# Role-to-Skill Matrix

This project is designed to cover the overlap among application engineering, cloud-native/platform engineering, factory automation IT, AI platform/MLOps, and data engineering roles.

| Capability | Why it matters | Project evidence |
|---|---|---|
| Python / backend engineering | Required across AI, platform, automation roles | FastAPI services, domain logic, workers |
| OOP / programming paradigms | Explicitly requested in application/platform roles | service/repository boundaries, composition |
| Algorithms & data structures | Common software engineering baseline | rate limiting, buffering, deduplication, efficient querying exercises |
| REST APIs | Full-stack/platform integration | machine, telemetry, alert, prediction APIs |
| SQL / PostgreSQL | Core application and data engineering | machine metadata + time-series telemetry persistence |
| NoSQL / Redis | caching and scalable state access | cache-aside, latest-state cache, stream/queue exercise |
| Testing | unit/function/integration requirements | pytest test pyramid and CI quality gate |
| Refactoring | explicit job responsibility | monolith evolves into cleaner modules/microservices |
| 12-factor app | explicitly requested | env config, stateless runtime, backing services, logs |
| Docker | containerized workloads | reproducible service images |
| Kubernetes | strongly preferred in multiple roles | Deployments, Services, probes, resources, HPA |
| Microservices | cloud-native architecture requirement | ingestion and ML service extraction |
| CI/CD | DevOps quality-control requirement | GitHub Actions test/build/deploy pipeline |
| Git / GitHub | explicit requirement | feature branches, PRs, automated checks |
| Prometheus / Grafana | SRE collaboration and monitoring | metrics, dashboards, alert rules |
| SLI / SLO / SLA | explicit SRE responsibilities | availability/latency/error/ingestion SLOs |
| Incident response | production sustainability | failure simulation + postmortem |
| Data pipeline | data platform and AI lifecycle | raw telemetry → cleaning/features → storage |
| S3 / MinIO | unstructured/object storage requirement | raw datasets + model artifacts |
| Batch / stream processing | big-data/data-engineering baseline | batch feature job + event-processing worker |
| ML/DL fundamentals | AI role requirement | anomaly detection model + error analysis |
| Model serving | AI platform responsibility | independently deployable prediction API |
| MLOps / ML lifecycle | explicit preferred qualification | experiment tracking, model registry, drift checks |
| GitOps / Argo CD | modern deployment/platform skill | desired-state K8s delivery from Git |

## Priority order

### Tier 1 — Must be interview-ready
Python, HTTP/REST, OOP, SQL, testing, Git, Docker, Kubernetes basics, CI/CD, SLI/SLO, Prometheus/Grafana.

### Tier 2 — Strong differentiators
Redis, microservice boundaries, data pipelines, object storage, ML serving, MLOps, GitOps.

### Tier 3 — Know the concepts, deepen later
Istio/service mesh, Cassandra, Hadoop/Spark, advanced distributed-system algorithms, large-scale production cluster administration.

The 120-hour project intentionally prioritizes depth in Tier 1 and practical exposure to Tier 2 rather than shallowly installing every technology listed in the job descriptions.
