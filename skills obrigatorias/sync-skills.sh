#!/usr/bin/env bash
set -Eeuo pipefail
umask 027

readonly REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
manifest="${SKILLS_MANIFEST:-$REPO_ROOT/skills/skills-manifest.json}"
target="${SKILLS_DESTINATION:-${LYVOX_ROOT:-/opt/lyvox}/skills/codex}"
sources="${SKILLS_SOURCE_PATHS:-}"
approval="${SKILLS_APPROVAL_FILE:-}"
apply=false
usage() { printf 'uso: %s --source DIR [--source DIR] [--manifest FILE] [--target DIR] [--approval FILE] [--apply]\n' "$0" >&2; exit 2; }
while (($#)); do
  case "$1" in
    --source) sources="${sources:+$sources:}${2:-}"; shift 2 ;;
    --manifest) manifest="${2:-}"; shift 2 ;;
    --target|--destination) target="${2:-}"; shift 2 ;;
    --approval) approval="${2:-}"; shift 2 ;;
    --apply) apply=true; shift ;;
    *) usage ;;
  esac
done
log() { printf '[skills-sync] %s\n' "$*"; }
die() { printf '[skills-sync] ERROR: %s\n' "$*" >&2; exit 1; }
as_root() { if (( EUID == 0 )); then "$@"; else command sudo "$@"; fi; }
command -v jq >/dev/null 2>&1 || die "jq obrigatório"
[[ -f "$manifest" && -n "$sources" ]] || usage
mapfile -t names < <(jq -er '.skills[] | select(.status | startswith("available")) | .name' "$manifest")
((${#names[@]} > 0)) || die "manifest sem skills disponíveis"
IFS=':' read -r -a roots <<<"$sources"
staging_root="$(mktemp -d)"; trap 'rm -rf -- "$staging_root"' EXIT

approved=0
for name in "${names[@]}"; do
  [[ "$name" =~ ^[A-Za-z0-9][A-Za-z0-9._-]*$ ]] || die "nome inseguro: $name"
  source_dir=''
  for root in "${roots[@]}"; do
    candidate="$root/$name"
    if [[ -f "$candidate/SKILL.md" && ! -L "$candidate" && ! -L "$candidate/SKILL.md" ]]; then source_dir="$candidate"; break; fi
  done
  [[ -n "$source_dir" ]] || die "skill disponível sem origem confiável: $name"
  if find "$source_dir" -type f \( -name '.env' -o -name '*.key' -o -name '*.pem' -o -name '*.db' -o -name '*.sqlite*' \) -print -quit | grep -q .; then die "arquivo proibido em $name"; fi
  if find "$source_dir" -type l -print -quit | grep -q .; then die "symlink interno em $name"; fi
  if grep -RIlE --exclude-dir=.git '(^|[^[:alnum:]_-])sk-(proj-)?[A-Za-z0-9_-]{20,}([^[:alnum:]_-]|$)|-----BEGIN .*PRIVATE KEY-----|AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9_]{30,}' "$source_dir" | grep -q .; then die "possível secret em $name"; fi # scanner-pattern-literal
  mkdir -p "$staging_root/files/$name"
  rsync -a --exclude='.git/' --exclude='.env*' --exclude='node_modules/' --exclude='dist/' --exclude='build/' "$source_dir/" "$staging_root/files/$name/"
  approved=$((approved + 1)); log "DRY-RUN aprovado: $name"
done
selection_manifest="$staging_root/SELECTION.sha256"
(cd "$staging_root/files" && find . -type f -print0 | sort -z | xargs -0 sha256sum >"$selection_manifest")
selection_hash="$(sha256sum "$selection_manifest" | awk '{print $1}')"
log "REVIEW_SELECTION_SHA256=$selection_hash"
if [[ "$apply" == false ]]; then log "$approved skill(s) aprovadas; crie aprovação e repita com --apply"; exit 0; fi
[[ -f "$approval" ]] || die "--apply exige arquivo --approval revisado"
approved_by="$(sed -n 's/^approved_by=//p' "$approval" | tail -n1)"
approved_hash="$(sed -n 's/^selection_sha256=//p' "$approval" | tail -n1)"
[[ -n "$approved_by" && "$approved_hash" == "$selection_hash" ]] || die "identidade/hash não corresponde ao conteúdo selecionado"
as_root install -d -m 0750 "$target"
for name in "${names[@]}"; do
  as_root install -d -m 0750 "$target/$name"
  as_root rsync -a --delete "$staging_root/files/$name/" "$target/$name/"
  log "sincronizada: $name"
done
log "$approved skill(s) sincronizadas a partir do conteúdo aprovado"
