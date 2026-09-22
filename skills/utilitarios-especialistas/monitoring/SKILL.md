# MONITORING_SKILL

Skill especializada em observabilidade, métricas, logs e tracing.

## Repositórios de Referência

- **Prometheus**: https://github.com/prometheus/prometheus
- **Grafana**: https://github.com/grafana/grafana
- **Sentry**: https://github.com/getsentry/sentry

## Capacidades

### 1. Prometheus
- Configurar Prometheus server
- Definir métricas (counters, gauges, histograms, summaries)
- Configurar service discovery
- Implementar Prometheus operators
- Escrever PromQL queries
- Configurar alerting rules
- Integrar com exporters

### Métricas Prometheus
```python
from prometheus_client import Counter, Histogram, Gauge

# Counter: valores que só incrementam
requests_total = Counter('http_requests_total', 'Total HTTP requests', ['method', 'status'])

# Gauge: valores que podem subir e descer
active_connections = Gauge('active_connections', 'Active connections')

# Histogram: distribuição de valores
request_duration = Histogram('request_duration_seconds', 'Request duration')

# Uso
requests_total.labels(method='GET', status='200').inc()
request_duration.observe(0.123)
```

### Prometheus Config
```yaml
global:
  scrape_interval: 15s

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']

rule_files:
  - 'alerts.yml'

scrape_configs:
  - job_name: 'api'
    static_configs:
      - targets: ['api:8000']
  - job_name: 'node'
    static_configs:
      - targets: ['node-exporter:9100']
```

### 2. Grafana
- Criar dashboards customizados
- Configurar datasources (Prometheus, Loki, etc.)
- Implementar alerting rules
- Criar variáveis e templates
- Configurar authentication (OAuth, LDAP)
- Usar Grafana HTTP API
- Implementar annotations

### Grafana Dashboard JSON
```json
{
  "panels": [
    {
      "title": "Requests per Second",
      "type": "timeseries",
      "targets": [
        {
          "expr": "rate(http_requests_total[5m])",
          "legendFormat": "{{method}} - {{status}}"
        }
      ]
    }
  ]
}
```

### 3. Sentry
- Configurar Sentry SDK
- Capturar exceptions automaticamente
- Implementar breadcrumb tracking
- Configurar release tracking
- Usar user context
- Configurar custom tags
- Implementar performance monitoring

### Sentry Python
```python
import sentry_sdk

sentry_sdk.init(
    dsn="https://key@sentry.io/project",
    traces_sample_rate=0.1,
    release="my-app@1.0.0",
    environment="production"
)

try:
    # código que pode falhar
    raise Exception("Erro de exemplo")
except Exception as e:
    sentry_sdk.capture_exception(e)

# Capturar mensagem
sentry_sdk.capture_message("Algo importante aconteceu", level="warning")
```

### 4. Logs e Tracing
- **Loki**: Agregação de logs
- **Jaeger**: Distributed tracing
- **Tempo**: Tracing.backend para Grafana
- **ELK Stack**: Elasticsearch, Logstash, Kibana

## O11y Stack Completo

| Componente | Função |
|------------|--------|
| Prometheus | Coleta de métricas |
| Grafana | Visualização |
| Alertmanager | Alertas |
| Loki | Logs |
| Jaeger/Tempo | Tracing |
| Sentry | Error tracking |

## Quando Usar

Use esta skill quando:
- Precisa implementar monitoring de aplicação
- Precisa criar dashboards de métricas
- Precisa configurar alertas
- Precisa rastrear errors com Sentry
- Precisa implementar observabilidade completa
- Precisa fazer debugging de produção