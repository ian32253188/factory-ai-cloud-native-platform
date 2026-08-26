# SLI / SLO Baseline

This document is a starting contract for the platform. The targets are not
attained measurements until dashboards and a representative load test produce
evidence.

## Initial service-level objectives

| SLO | Target | Window | Scope |
| --- | ---: | --- | --- |
| API availability | 99.5% | 30 rolling days | Versioned API requests excluding deliberate client errors |
| API latency | 95% under 300 ms | 30 rolling days | Successful read endpoints in the local reference environment |
| API server errors | < 1% | 30 rolling days | HTTP 5xx responses |
| Reading-ingestion freshness | 99% under 60 s | 7 rolling days | Accepted readings visible to analytics |
| Alert processing freshness | 99% under 120 s | 7 rolling days | Alert decision emitted after an accepted reading |

The targets are intentionally modest for a learning platform. They must be
revisited after the deployment topology, traffic shape, and data volume are
known.

## SLI definitions

### Availability

```text
good_events = requests with HTTP status < 500
total_events = all requests to the measured API routes
availability = good_events / total_events
```

4xx responses remain visible as a separate client-error metric. Health probes
and administrative endpoints should not silently inflate the user-facing
availability calculation.

### Latency

Measure request duration at the API boundary and report histogram quantiles.
The dashboard should show p50, p95, and p99 by route and status class; the SLO
uses p95 for the initial baseline.

### Freshness

Record both event time and processing/visibility time. Freshness is the elapsed
time between the accepted event timestamp and the time the downstream consumer
can query the result. Clock assumptions and late-arriving data must be
documented with the metric.

## Error budget

For a 30-day 99.5% availability target, the initial budget is approximately
3 hours 36 minutes of measured unavailability. The budget is a decision aid:

- healthy budget: continue feature delivery and small reliability improvements;
- warning budget: prioritise testing, capacity, and operational fixes;
- exhausted budget: pause risky feature work until the reliability issue has a
  verified mitigation.

## Alerting principles

- Alert on symptoms users experience, not every low-level metric fluctuation.
- Use a short, actionable summary with dashboard and runbook links.
- Separate paging-worthy incidents from tickets and trend notifications.
- Test alert rules with synthetic metric samples before relying on them.
- Every alert must have an owner, severity, and a documented first response.

## Evidence required before claiming SLO compliance

- instrumented metric definitions in source;
- dashboard queries checked against emitted metrics;
- alert-rule validation;
- a documented load or availability test with environment and time window;
- an incident or failure-mode drill for the main dependency path.
