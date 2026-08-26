# Test strategy

The project will maintain three complementary layers:

1. unit tests for domain rules and pure transformations;
2. integration tests for SQL, Redis, and service adapters;
3. API/contract tests for HTTP behaviour and service boundaries.

Each layer should run locally and in CI with deterministic synthetic data.
