# Architecture Evolution

The architecture is intentionally evolutionary. Each stage exists to teach *why* the next stage is needed.

## Stage 1 — Production-shaped monolith

```text
Client
  |
FastAPI
  |
Router -> Service -> Repository
                     |
                 PostgreSQL
```

Learn:
- HTTP/REST
- layering and dependency boundaries
- SQL and transactions
- testing
- configuration
- refactoring

Why start here?
Because distributed systems add network latency, partial failure, deployment complexity, observability needs, and operational cost. A clean monolith is the baseline from which those tradeoffs become visible.

## Stage 2 — Containerized application

```text
Docker Compose
├── API
├── PostgreSQL
└── Redis
```

Learn:
- image vs container
- networking and service discovery
- persistent volumes
- runtime configuration
- caching

## Stage 3 — First service extraction

```text
             +------------------+
Devices ---> | Ingestion Service|
             +---------+--------+
                       |
                  PostgreSQL
                       |
                   Core API
```

Extract only when there is a concrete reason: independent scaling, failure isolation, or a clearly separate responsibility.

Learn:
- service boundaries
- API contracts
- timeouts/retries
- idempotency
- distributed failure

## Stage 4 — Data + AI platform

```text
Ingestion -> PostgreSQL -> Feature Pipeline -> MinIO
                               |              |
                               v              v
                           Training ------> Model
                                              |
                                              v
                                         ML Service
```

Learn:
- batch pipeline
- object storage
- reproducibility
- model lifecycle
- online inference

## Stage 5 — Kubernetes

```text
Kubernetes Cluster
├── ingestion Deployment + Service
├── api Deployment + Service
├── ml Deployment + Service
├── worker Deployment
├── ConfigMaps / Secrets
└── HPA / probes / resource controls
```

Learn:
- desired state
- reconciliation
- scheduling
- service discovery
- health probes
- resource management
- autoscaling

## Stage 6 — SRE and observability

```text
Apps -> /metrics -> Prometheus -> Grafana
                    |
                    +-> Alert rules
```

Initial SLIs:
- HTTP availability
- p95 request latency
- server error ratio
- telemetry ingestion success ratio
- ML inference latency/error ratio

Example SLOs for the learning environment:
- API successful-request ratio >= 99.5% over 7 days
- p95 API latency < 300 ms
- telemetry ingestion success >= 99.9%

The exact target values are less important than learning how to calculate, monitor, and respond to them.

## Stage 7 — CI/CD and GitOps

```text
Developer -> GitHub PR
               |
          GitHub Actions
      lint -> test -> image
               |
              Git
               |
            Argo CD
               |
          Kubernetes
```

Learn:
- immutable artifacts
- quality gates
- desired-state deployment
- rollback
- reconciliation

# Architectural Decision Questions

Before introducing a technology, answer:

1. What problem do we currently have?
2. Why can't the current design solve it sufficiently?
3. What complexity does the new technology add?
4. How will we test it?
5. How will we observe it in production?
6. How will we recover when it fails?

These questions are more valuable in interviews than simply listing technologies.
