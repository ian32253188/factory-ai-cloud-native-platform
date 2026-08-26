# 30-Day / 120-Hour Learning Roadmap

This roadmap uses a **learn → build → verify → explain** loop. Assume about 4 hours per day.

## Rule for every day

1. Learn the minimum theory needed for today's feature.
2. Implement one observable behavior in this repository.
3. Verify it with tests, commands, or metrics.
4. Write a short note explaining *why* the technology exists and what problem it solved.

---

## Week 1 — Software Engineering Foundations (28h)

### Day 1 — HTTP, REST, FastAPI, Git (4h)
**Learn (1.5h)**
- client/server model
- IP, port, URL, HTTP request/response
- HTTP methods: GET, POST, PUT, PATCH, DELETE
- status codes: 2xx, 4xx, 5xx
- REST resources and idempotency
- Python virtual environments, modules, type hints
- Git working tree, commit, branch

**Build (2h)**
- run the FastAPI application
- inspect `/docs`
- call `/health`
- create `/api/v1/machines` GET endpoint with an in-memory list

**Verify & explain (0.5h)**
- run pytest
- explain why `GET /machines` should not mutate state

### Day 2 — Python OOP and application layering (4h)
**Learn**
- class vs object
- encapsulation
- composition vs inheritance
- interface / dependency boundary
- separation of concerns
- controller/router → service → repository

**Build**
- Machine domain model
- MachineService
- in-memory MachineRepository
- router calls service instead of accessing data directly

**Verify**
- unit tests for service
- explain why router should not contain business logic

### Day 3 — SQL and relational data modeling (4h)
**Learn**
- table, row, primary key, foreign key
- normalization basics
- SELECT/INSERT/UPDATE/DELETE
- index and its tradeoff
- transaction and ACID
- ORM vs raw SQL

**Build**
- PostgreSQL schema for machines and telemetry
- SQLAlchemy models
- repository backed by PostgreSQL

**Verify**
- integration test against test database
- inspect generated SQL

### Day 4 — Testing and software quality (4h)
**Learn**
- test pyramid
- unit vs integration vs functional vs E2E
- arrange/act/assert
- mocking and when not to mock
- code coverage limits

**Build**
- unit tests for business rules
- API tests with FastAPI TestClient
- database integration tests

**Verify**
- intentionally introduce a bug and ensure tests catch it

### Day 5 — Refactoring and design principles (4h)
**Learn**
- cohesion and coupling
- SOLID overview
- dependency inversion
- DRY vs premature abstraction
- code smell
- refactoring vs rewriting

**Build**
- refactor machine and telemetry logic
- introduce interfaces/protocols only where useful

**Verify**
- tests stay green before and after refactor

### Day 6 — Configuration and Twelve-Factor principles (4h)
**Learn**
- config vs code
- environment variables
- stateless processes
- backing services
- logs as event streams
- dev/prod parity

**Build**
- environment-based configuration
- `.env.example`
- structured application settings

**Verify**
- change behavior using environment variables without editing code

### Day 7 — Week 1 architecture review (4h)
**Learn**
- monolith vs distributed system
- latency, partial failure, network boundaries
- why microservices are not automatically better

**Build**
- complete production-shaped monolith
- architecture diagram v1

**Explain**
- 10-minute mock interview: explain current architecture and tradeoffs

---

## Week 2 — Containers, Data, Microservices (28h)

### Day 8 — Linux process and networking basics (4h)
Learn processes, signals, ports, localhost, DNS, TCP basics, environment variables, file permissions.

Build and debug the app from command line only.

### Day 9 — Docker fundamentals (4h)
Learn image vs container, layers, Dockerfile, build context, registry, volume, network.

Build a Docker image for the API and run it locally.

### Day 10 — Docker Compose + PostgreSQL (4h)
Learn container networking, service discovery, volumes, startup dependencies.

Build API + PostgreSQL with Compose.

### Day 11 — Redis and caching (4h)
Learn cache-aside, TTL, cache invalidation, persistence tradeoffs.

Add Redis for latest machine state / expensive query caching.

### Day 12 — Messaging and asynchronous processing (4h)
Learn synchronous vs asynchronous communication, queue, producer/consumer, at-least-once delivery, idempotent consumer.

Implement a simple event-processing worker (Redis Streams or similar lightweight mechanism).

### Day 13 — Microservice boundaries (4h)
Learn bounded context, database-per-service idea, API contract, distributed failure, retries/timeouts.

Extract telemetry ingestion from the monolith into a separate service.

### Day 14 — Object storage + data pipeline (4h)
Learn object storage, S3 concepts, batch vs stream, ETL/ELT, schema evolution.

Store raw telemetry batches in MinIO and build a simple feature pipeline.

---

## Week 3 — Kubernetes, CI/CD, SRE (36h)

### Day 15 — Kubernetes mental model (4h)
Learn cluster, control plane, node, Pod, Deployment, ReplicaSet, Service, desired state.

Deploy one API to local Kubernetes (kind or minikube).

### Day 16 — Kubernetes configuration (4h)
Learn ConfigMap, Secret, namespace, labels, selectors.

Move runtime configuration into Kubernetes resources.

### Day 17 — Reliability primitives (4h)
Learn liveness, readiness, startup probes; resource request/limit; graceful shutdown.

Add probes and resource controls.

### Day 18 — Scaling and networking (4h)
Learn horizontal scaling, HPA, ingress/gateway basics, statelessness.

Scale API replicas and generate load.

### Day 19 — CI fundamentals (4h)
Learn CI vs CD, pipeline, artifact, immutable build, quality gate.

GitHub Actions: lint → test → build image.

### Day 20 — CD and deployment strategies (4h)
Learn rolling deployment, rollback, blue/green, canary concepts.

Automate deployment to local/test K8s environment where practical.

### Day 21 — Observability fundamentals (4h)
Learn metrics/logs/traces, RED method, USE method, cardinality.

Instrument request count, error count, latency, telemetry ingest count.

### Day 22 — Prometheus + Grafana (4h)
Learn scrape model, counter/gauge/histogram, PromQL basics.

Create dashboard for availability, latency, throughput, errors.

### Day 23 — SLI / SLO / Error Budget (4h)
Learn SLI, SLO, SLA, error budget, burn rate.

Define measurable reliability targets and document them.

---

## Week 4 — AI Platform, MLOps, GitOps (28h)

### Day 24 — ML lifecycle refresher (4h)
Learn problem framing, train/validation/test split, leakage, baseline, features, metrics, error analysis.

Create anomaly-detection baseline from telemetry.

### Day 25 — Model serving (4h)
Learn online vs batch inference, model serialization, feature consistency, inference latency.

Expose `/predict` in an ML service.

### Day 26 — Model lifecycle / MLflow (4h)
Learn experiment tracking, model registry, artifact, versioning, reproducibility.

Track model experiments and register the selected model.

### Day 27 — MLOps quality (4h)
Learn data drift, concept drift, model monitoring, retraining trigger, feature quality.

Add model metrics and a drift-check job.

### Day 28 — GitOps / Argo CD (4h)
Learn desired-state deployment, reconciliation loop, Git as source of truth.

Create Kubernetes manifests or Helm/Kustomize structure managed through Git.

### Day 29 — Production incident exercise (4h)
Simulate latency/errors/dependency failure.

Use dashboard + logs + SLO to diagnose; write a mini postmortem.

### Day 30 — Portfolio + interview demo (4h)
- clean README
- final architecture diagram
- record demo flow
- document design decisions and tradeoffs
- prepare 15 interview questions and answers
- compare final architecture with Day 1 monolith

---

# Core Knowledge Checklist

## Programming
- Python syntax and type hints
- OOP and composition
- exception handling
- async/await basics
- data structures and Big-O

## Backend
- HTTP/REST
- API design
- validation
- dependency injection
- SQL and transactions
- caching
- background processing

## Software Engineering
- Git
- testing pyramid
- SOLID
- clean boundaries
- refactoring
- code review mindset
- 12-factor application

## DevOps / Cloud Native
- Linux/process/network basics
- Docker
- Compose
- CI/CD
- Kubernetes
- configuration/secrets
- probes/resources/autoscaling

## SRE
- availability
- latency
- throughput
- errors
- observability
- SLI/SLO/SLA
- error budget
- alert design
- incident response

## Data Engineering
- SQL/NoSQL tradeoffs
- batch vs stream
- ETL/ELT
- object storage
- schema/data quality
- pipeline reliability

## AI / MLOps
- ML problem framing
- feature engineering
- evaluation/error analysis
- model serving
- experiment tracking
- model registry
- drift
- retraining

# Recommended official resources

Use official documentation first; tutorials are for targeted gaps.

- Python: https://docs.python.org/3/tutorial/
- FastAPI: https://fastapi.tiangolo.com/tutorial/
- PostgreSQL Tutorial: https://www.postgresql.org/docs/current/tutorial.html
- pytest: https://docs.pytest.org/
- Twelve-Factor App: https://12factor.net/
- Docker: https://docs.docker.com/get-started/
- Redis: https://redis.io/docs/latest/
- Kubernetes: https://kubernetes.io/docs/tutorials/
- GitHub Actions: https://docs.github.com/actions
- Prometheus: https://prometheus.io/docs/introduction/overview/
- Grafana: https://grafana.com/docs/
- MLflow: https://mlflow.org/docs/latest/
- MinIO: https://min.io/docs/minio/container/index.html
- Argo CD: https://argo-cd.readthedocs.io/en/stable/getting_started/
