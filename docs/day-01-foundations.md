# Day 01 — HTTP, REST, FastAPI, Git

Goal: understand what happens between a client sending a request and the application returning a response.

## 1. Client / Server mental model

A client initiates a request. A server listens on a network address and returns a response.

Example:

```text
Browser / curl
     |
     | HTTP GET /health
     v
FastAPI application
     |
     | JSON response
     v
Client
```

Important terms:
- IP address: identifies a host on a network.
- Port: identifies a process/service endpoint on that host.
- URL: tells the client where and what resource to request.
- HTTP: application-layer protocol used to exchange requests and responses.

## 2. Anatomy of an HTTP request

Conceptually:

```text
GET /health HTTP/1.1
Host: localhost:8000
Accept: application/json
```

A request includes:
- method
- path/URL
- headers
- optional body

A response includes:
- status code
- headers
- optional body

## 3. HTTP methods

### GET
Read a resource. It should not change server state as a side effect.

### POST
Create a resource or trigger an operation.

### PUT
Replace the representation of a resource. Usually designed to be idempotent.

### PATCH
Partially update a resource.

### DELETE
Delete a resource. Often designed to be idempotent from the client's perspective.

## 4. Idempotency

An operation is idempotent if performing it multiple times has the same intended effect as performing it once.

Example:

```text
PUT /machines/123 {"status": "offline"}
```

Sending the same request twice should still leave machine 123 offline.

Why it matters:
- clients retry requests;
- distributed systems fail partially;
- networks can time out even when the server completed the action.

## 5. Common HTTP status codes

- `200 OK`: request succeeded.
- `201 Created`: resource created.
- `204 No Content`: succeeded without response body.
- `400 Bad Request`: invalid request semantics.
- `401 Unauthorized`: authentication is required/invalid.
- `403 Forbidden`: caller is identified but lacks permission.
- `404 Not Found`: resource does not exist.
- `409 Conflict`: request conflicts with current state.
- `422 Unprocessable Content`: validation/semantic input problem; commonly seen in FastAPI validation.
- `500 Internal Server Error`: unexpected server failure.
- `503 Service Unavailable`: service cannot currently handle the request.

## 6. What FastAPI is doing for us

In this repository:

```python
@router.get("/health")
def health_check() -> dict[str, str]:
    ...
```

FastAPI:
1. registers the route;
2. matches an incoming `GET /health` request;
3. calls the Python function;
4. serializes the returned dictionary to JSON;
5. creates the HTTP response;
6. automatically exposes the endpoint in OpenAPI/Swagger documentation.

## 7. Why `create_app()` exists

Instead of placing all configuration directly at module level, we use an application factory:

```python
def create_app() -> FastAPI:
    app = FastAPI(...)
    app.include_router(health_router)
    return app
```

Benefits:
- easier testing;
- clearer application assembly;
- easier environment-specific setup later;
- dependencies can be introduced without turning one file into a giant script.

## 8. Why configuration is outside source code

`app/core/config.py` reads settings from environment variables.

This separates:

```text
Code: how the application behaves
Config: which environment it is running in
```

Later the same container image can run in development, test, staging, and production with different configuration.

This connects directly to Twelve-Factor App principles.

## 9. What the health endpoint means

`GET /health` currently answers a simple question:

> Is the application process alive and capable of serving a request?

Later we will distinguish:
- liveness: should the process be restarted?
- readiness: should traffic be sent to this instance?
- startup: has slow initialization completed?

These become important when Kubernetes is introduced.

## 10. What the test proves

`tests/test_health.py` sends a real HTTP-style request through FastAPI's test client.

```python
response = client.get("/health")
assert response.status_code == 200
```

It protects behavior. When we refactor later, the test tells us whether the externally visible behavior still works.

## Hands-on exercises

### Exercise A — Run the service

```bash
uvicorn app.main:app --reload
```

Visit:

```text
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/health
```

### Exercise B — Call it without a browser

```bash
curl http://127.0.0.1:8000/health
```

Explain what is the client and what is the server.

### Exercise C — Change config without editing Python

Create `.env`:

```env
FACTORY_ENVIRONMENT=practice
```

Restart the server and observe the `/health` response.

### Exercise D — Create your first resource endpoint

Implement:

```text
GET /api/v1/machines
```

Return three in-memory machines. Do not add a database yet.

Suggested response:

```json
[
  {"id": "M-001", "name": "Bonder-01", "status": "running"},
  {"id": "M-002", "name": "Bonder-02", "status": "idle"}
]
```

Then add a test.

## Interview checkpoints

You should be able to answer these without notes:

1. What is the difference between HTTP and REST?
2. Why is GET supposed to be safe?
3. What does idempotent mean and why do retries make it important?
4. What is the difference between `404` and `500`?
5. What is an application health endpoint?
6. Why should configuration come from the environment?
7. Why do we write a test before refactoring?
8. What happens from `curl /health` to the JSON response?

## Definition of done

Day 1 is complete when:
- the app runs locally;
- `/health` returns 200;
- pytest passes;
- you have implemented and tested `GET /api/v1/machines` yourself;
- you can explain all eight interview checkpoints in your own words.

## References

- FastAPI Tutorial: https://fastapi.tiangolo.com/tutorial/
- FastAPI Testing: https://fastapi.tiangolo.com/tutorial/testing/
- MDN HTTP Overview: https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
- HTTP Semantics (RFC 9110): https://www.rfc-editor.org/rfc/rfc9110
- Twelve-Factor App: https://12factor.net/
- GitHub Git Handbook: https://docs.github.com/en/get-started/using-git/about-git
