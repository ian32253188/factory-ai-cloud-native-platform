# Architecture

## Purpose

The platform models a factory-monitoring workflow: sensor readings enter the
system, are stored and analysed, and can produce operator alerts. A later ML
path provides predictions or anomaly scores through a versioned inference API.

The architecture is designed to teach delivery skills in a sequence that keeps
each stage demonstrable and testable.

## Evolution plan

| Stage | Primary outcome | Boundary |
| --- | --- | --- |
| 1. Modular monolith | REST API, SQL persistence, validation, tests | `apps/api` modules |
| 2. Containerised app | Reproducible local runtime | `infrastructure/docker` |
| 3. Delivery baseline | Automated lint and test checks | `.github/workflows` |
| 4. Resilience and extraction | Redis usage and service contracts | `services/` |
| 5. Kubernetes platform | Deployable workloads, config, probes | `infrastructure/kubernetes` and `helm` |
| 6. Observability and SRE | Metrics, dashboards, SLI/SLO, alerts | `observability/` and `docs/sli-slo.md` |
| 7. Data and ML | Validated data flow and inference API | `data/pipeline` and `services/ml-service` |
| 8. GitOps | Declarative promotion and drift visibility | `infrastructure/argocd` |

## Day 1 logical design

The first API is a modular monolith with explicit domain modules:

- `sensors`: sensor identity, metadata, and status
- `readings`: timestamped measurements and validation
- `analytics`: aggregations and anomaly candidates
- `alerts`: alert state, severity, acknowledgement, and notification intent
- `health`: liveness, readiness, and dependency checks

The API owns the initial write path and SQL transaction boundary. A future
event contract will allow sensor ingestion and analytics to be extracted
without changing the operator-facing API contract.

## Proposed request flow

```text
sensor or simulator
        |
        v
POST /api/v1/readings  --> validation --> SQL transaction
                                      |
                                      +--> analytics candidate
                                      +--> alert decision
                                      +--> metrics
```

The first version may execute analytics synchronously for clarity. Background
processing and Redis-backed idempotency are introduced only after the baseline
behaviour is covered by tests.

## Data ownership

| Data | Initial owner | Future owner |
| --- | --- | --- |
| Sensor metadata | API / SQL | Sensor service |
| Raw readings | API / SQL | Sensor service or ingestion store |
| Aggregates | API / SQL | Analytics service |
| Alert lifecycle | API / SQL | Alert service |
| Features and model metadata | Data/ML modules | ML platform boundary |

No real factory data, credentials, model binaries, or secrets belong in this
repository. Examples and fixtures must be synthetic or openly redistributable.

## Non-functional requirements

- API contracts are versioned under `/api/v1`.
- Invalid input fails with a stable error shape and does not partially commit.
- Health endpoints distinguish process liveness from dependency readiness.
- Tests run without external cloud services.
- Metrics expose request count, latency, errors, and dependency failures.
- Every asynchronous boundary has an idempotency and retry story before it is
  considered production-shaped.

## Open decisions

- PostgreSQL versus another SQL engine for the first deployed environment
- Event transport after the synchronous baseline (Redis Streams, a broker, or
  an in-process outbox)
- UI framework and authentication model
- Model family, feature store approach, and model registry

These decisions should be made in ADRs when implementation evidence requires
them, rather than being hidden in configuration.
