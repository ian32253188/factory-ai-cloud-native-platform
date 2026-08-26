# ADR 0001: Start with a Modular Monolith

- Status: Accepted
- Date: 2026-08-26

## Context

The platform is intended to demonstrate both application fundamentals and
cloud-native operations. Starting with multiple deployable services would add
network, deployment, and debugging complexity before the domain behaviour and
test baseline are understood.

## Decision

Build the first factory-monitoring API as a modular monolith under `apps/api`.
Keep domain modules and dependency directions explicit, expose versioned REST
contracts, and extract services only after their behaviour is covered by tests
and their ownership is documented.

## Consequences

Positive consequences:

- faster feedback while learning Python, HTTP, REST, SQL, and testing;
- simple local setup and transaction boundaries;
- a clear baseline against which service extraction can be compared;
- fewer distributed-systems failure modes during the first milestone.

Trade-offs:

- the first deployment does not demonstrate independent service scaling;
- module boundaries must be actively protected from shortcuts;
- later extraction requires explicit contracts, retries, and observability.

## Exit criteria for extraction

A module may become a service when it has a stable API/event contract, an owner,
independent tests, health and metrics requirements, a data-ownership decision,
and a documented failure/retry strategy.
