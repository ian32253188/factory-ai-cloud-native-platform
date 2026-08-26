# 30-Day / 120-Hour Learning Roadmap

## Outcome

By the end of 30 days, the repository should tell one coherent engineering
story: a tested factory-monitoring API evolved into observable, Kubernetes-ready
services with a documented ML inference path and GitOps direction.

The hours below total exactly **120 hours**. They are a learning budget, not a
claim that every future production feature is already implemented.

## Daily plan

| Day | Focus | Deliverable | Hours |
| ---: | --- | --- | ---: |
| 1 | Repository, architecture, and Git workflow | Baseline docs, branch model, initial Issues | 4 |
| 2 | Python application structure | API package and configuration skeleton | 4 |
| 3 | HTTP and REST | Versioned health and sensor endpoints | 4 |
| 4 | SQL fundamentals | Schema, repository layer, and migrations plan | 4 |
| 5 | Validation and errors | Stable request/response and error contracts | 4 |
| 6 | Software architecture | Module boundaries and dependency direction | 4 |
| 7 | Unit testing | Domain and repository unit-test baseline | 4 |
| 8 | Integration and API testing | Database and HTTP integration tests | 4 |
| 9 | Git collaboration | Feature branch, review checklist, and history hygiene | 3 |
| 10 | Docker | Reproducible API image and local Compose path | 5 |
| 11 | CI/CD | Automated lint, tests, and artifact checks | 4 |
| 12 | Image quality | Build caching, security baseline, and smoke test | 4 |
| 13 | Redis | Idempotency, caching, and failure behaviour | 4 |
| 14 | Service extraction | Sensor-service boundary and contract | 4 |
| 15 | Service extraction | Analytics-service boundary and contract | 4 |
| 16 | Event contracts | Alert flow, retries, and contract tests | 4 |
| 17 | Kubernetes | Deployment, Service, and namespace manifests | 5 |
| 18 | Kubernetes operations | Config, secrets references, probes, and resources | 4 |
| 19 | Helm | Parameterised chart for the platform workloads | 4 |
| 20 | Local cluster delivery | Deploy, inspect, troubleshoot, and document | 5 |
| 21 | Prometheus | Application and platform metrics | 4 |
| 22 | Grafana | Operator and service-health dashboards | 4 |
| 23 | Telemetry | Structured logs and tracing baseline | 4 |
| 24 | SLI/SLO | Availability, latency, error, and freshness definitions | 4 |
| 25 | SRE operations | Alert rules, runbooks, and error-budget response | 4 |
| 26 | Data pipeline | Ingestion, schema validation, and bad-record handling | 4 |
| 27 | Features and lineage | Reproducible feature dataset and version metadata | 4 |
| 28 | ML API | Versioned inference endpoint and model health checks | 4 |
| 29 | MLOps and Argo CD | Promotion path, model metadata, and GitOps design | 4 |
| 30 | Capstone and career artifact | Demo script, evidence index, and resume bullets | 2 |
| **Total** |  |  | **120** |

## Milestones

### Milestone 1 — API foundation (Days 1–8, 32 hours)

The API can accept and retrieve synthetic sensor data, persists it through a
clear repository boundary, and has unit, integration, and API tests.

### Milestone 2 — Delivery and service boundaries (Days 9–16, 32 hours)

The application is containerised, checked by CI, uses Redis for a defined
problem, and documents extraction contracts for sensor, analytics, and alert
responsibilities.

### Milestone 3 — Kubernetes and operations (Days 17–25, 38 hours)

The platform has a local Kubernetes deployment path, dashboards, useful
metrics, initial SLI/SLO definitions, and actionable alert runbooks.

### Milestone 4 — Data, ML, and portfolio proof (Days 26–30, 18 hours)

The data and inference path is reproducible enough to explain, and the final
demo distinguishes implemented evidence from planned follow-up work.

## Working rules

1. Keep changes small enough to review on a feature branch.
2. Add a test or an explicit verification command with each runtime feature.
3. Record architectural changes in an ADR when they affect boundaries or
   operations.
4. Do not commit secrets, private datasets, credentials, or large model files.
5. Mark work as planned, implemented, or verified; do not blur those states in
   README claims.
