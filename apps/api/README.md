# API application

This directory is the first implementation target: a Python modular monolith
for factory monitoring.

Planned initial capabilities:

- `GET /healthz` for process liveness;
- `GET /readyz` for dependency readiness;
- versioned sensor and reading REST endpoints;
- SQL repository boundary with synthetic fixtures;
- stable validation and error responses;
- OpenAPI documentation generated from the API contract.

The runtime is not implemented in the Day 1 baseline yet. See the first API
GitHub Issue and [`docs/architecture.md`](../../docs/architecture.md).
