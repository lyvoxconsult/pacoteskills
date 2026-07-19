#!/usr/bin/env bash
set -Eeuo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; target="${LYVOX_ROOT:-/opt/lyvox}/skills"
if [[ "${1:-}" == --target ]]; then target="${2:-}"; [[ -n "$target" ]] || exit 2; elif (($#)); then echo "uso: $0 [--target DIR]" >&2; exit 2; fi
mkdir -p "$target/mandatory" "$target/catalog"
for file in mandatory-10-skills.md README.md; do [[ -f "$REPO_ROOT/skills/$file" ]] && install -m 0640 -C "$REPO_ROOT/skills/$file" "$target/mandatory/$file"; done
[[ -f "$REPO_ROOT/skills/skills-manifest.json" ]] && install -m 0640 -C "$REPO_ROOT/skills/skills-manifest.json" "$target/skills-manifest.json"
for file in "$REPO_ROOT"/skills/*-skills.md; do [[ -e "$file" ]] || continue; install -m 0640 -C "$file" "$target/catalog/$(basename "$file")"; done
echo "[skills] catálogo instalado em $target sem copiar diretórios pessoais"
