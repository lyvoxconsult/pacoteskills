---
name: monitoring-skill
description: Use for observability, metrics, logs, tracing, alerts, dashboards, Prometheus, Grafana, Sentry, error tracking, SLOs, production debugging, incident review, and operational signal design. Trigger when adding production features, background jobs, integrations, critical paths, or diagnosing runtime failures.
---

# Monitoring Skill

Use this skill to make important behavior observable before it fails silently.

Reference repositories:
- https://github.com/prometheus/prometheus
- https://github.com/grafana/grafana
- https://github.com/getsentry/sentry

## Workflow

1. Identify the user-visible or business-critical outcome to monitor.
2. Define signals: metrics for rates and latency, logs for decisions, traces for cross-boundary timing, errors for exceptions.
3. Keep labels low-cardinality and safe; do not leak secrets or personal data.
4. Add alerts only for actionable failures with a clear owner and threshold.
5. Build dashboards around diagnosis paths, not decorative charts.
6. Verify that signals are emitted in success and failure paths.

## Review Checklist

- Critical flows expose enough context to debug failures.
- Alerts have severity, threshold, and action.
- Error grouping includes useful context without sensitive data.
- Dashboards separate symptoms from causes.
- Monitoring does not add material latency or noisy logs.
