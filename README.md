# Factory AI Cloud-Native Platform

A 30-day / 120-hour hands-on project for learning production-grade software engineering, cloud-native architecture, SRE, DevOps, data engineering, and MLOps through one evolving factory AI platform.

## Goal

Build a factory equipment monitoring and AI anomaly-detection platform that evolves through four stages:

1. **Production-ready monolith** — FastAPI, REST, OOP, testing, SQL, configuration, 12-factor principles.
2. **Cloud-native services** — Docker, PostgreSQL, Redis, microservices, data pipeline, object storage.
3. **Kubernetes + SRE** — K8s, health probes, autoscaling, Prometheus, Grafana, SLI/SLO, alerting.
4. **AI platform + GitOps** — ML lifecycle, model service, batch features, MLflow/MinIO, CI/CD, Argo CD.

The point is not to collect tool names. Every technology must solve a concrete problem in the same system.

## Product Scenario

A factory has multiple machines sending telemetry such as temperature, vibration, current, pressure, and throughput. The platform will:

- ingest equipment telemetry;
- store and query machine state and historical measurements;
- expose REST APIs for operators and other applications;
- detect abnormal machine behavior with an ML model;
- create alerts when operational or AI thresholds are exceeded;
- expose service and business metrics;
- run as containerized workloads on Kubernetes;
- define SLI/SLO and production alerts;
- automate test, build, deploy, and model lifecycle workflows.

## Target Architecture

```text
Telemetry Generator / Factory Devices
              |
              v
      Ingestion API / Service
              |
       +------+-------+
       |              |
       v              v
 PostgreSQL         Redis
       |
       +--------> Data / Feature Pipeline ----> MinIO
                                      |             |
                                      v             v
                                 ML Training --> Model Artifact
                                                   |
                                                   v
                                              ML Service
                                                   |
                                                   v
                                              Alert Service

                  API / services
                       |
                Kubernetes / Argo CD
                       |
          Prometheus + Grafana + Alerting
```

We will **not** start here. We begin with a monolith and refactor toward this architecture so the architectural decisions are learned rather than copied.

## Current Phase — Phase 1

Start with the smallest production-shaped application:

```text
app/
├── main.py
├── core/
│   └── config.py
└── api/
    └── health.py

tests/
└── test_health.py
```

### First learning objectives

Before adding more features, be able to explain:

- process vs thread vs async I/O;
- HTTP request/response and REST semantics;
- status codes and idempotency;
- Python modules, type hints, classes, dependency boundaries;
- configuration vs source code;
- unit, integration, functional, and end-to-end tests;
- what an application health endpoint is and why orchestration systems need it.

## Run locally

Python 3.12+ is recommended.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -e ".[dev]"
```

Run:

```bash
uvicorn app.main:app --reload
```

Open:

- API docs: `http://127.0.0.1:8000/docs`
- Health: `http://127.0.0.1:8000/health`

Tests:

```bash
pytest
```

## 120-hour roadmap

| Phase | Hours | Outcome |
|---|---:|---|
| 1. Software foundations + production monolith | 24 | REST API, OOP, SQL, tests, refactoring, 12-factor |
| 2. Containers + data + microservices | 30 | Docker/Compose, PostgreSQL, Redis, MinIO, service boundaries |
| 3. Kubernetes + DevOps + SRE | 36 | K8s, CI/CD, metrics, dashboards, SLI/SLO, alerts |
| 4. AI/MLOps + GitOps integration | 30 | model lifecycle, ML API, batch pipeline, MLflow, Argo CD |
| **Total** | **120** | portfolio-ready cloud-native AI platform |

Detailed daily plan: [`docs/learning-roadmap.md`](docs/learning-roadmap.md)

Role-to-skill mapping: [`docs/skill-matrix.md`](docs/skill-matrix.md)

Architecture evolution: [`docs/architecture.md`](docs/architecture.md)

## Engineering principles

- Learn the problem before adding the tool.
- Keep components independently testable.
- Prefer observable failure over silent failure.
- Configuration comes from the environment.
- Automate repeatable checks.
- Every production feature needs a way to verify it.
- Refactor only after behavior is protected by tests.
- Define reliability with measurable indicators, not feelings.

## Official learning references

- FastAPI Tutorial: https://fastapi.tiangolo.com/tutorial/
- FastAPI Testing: https://fastapi.tiangolo.com/tutorial/testing/
- Docker Get Started: https://docs.docker.com/get-started/
- Kubernetes Concepts: https://kubernetes.io/docs/concepts/
- GitHub Actions: https://docs.github.com/actions
- Prometheus Docs: https://prometheus.io/docs/
- Grafana Docs: https://grafana.com/docs/
- Argo CD Docs: https://argo-cd.readthedocs.io/
- Twelve-Factor App: https://12factor.net/

## Definition of Done for the month

By the end, you should be able to demo the system and explain—not merely name—the following:

`Python` · `FastAPI` · `REST` · `OOP` · `SQL` · `pytest` · `Git` · `Docker` · `Docker Compose` · `PostgreSQL` · `Redis` · `Microservices` · `Kubernetes` · `CI/CD` · `Prometheus` · `Grafana` · `SLI/SLO` · `Alerting` · `Data Pipeline` · `MinIO/S3` · `ML Lifecycle` · `MLOps` · `Argo CD / GitOps`
