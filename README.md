# CI/CD Assignment Project

## Overview
About this project:
- a FastAPI app
- a Dockerfile
- a GitHub Actions workflow

Main endpoints:
- `GET /health` → `{"status": "healthy"}`
- `GET /version` → `{"version": "1.0.0"}`
- `GET /` → welcome message

The app also logs each request method and path in the server output.

---

## What I chose to implement
I used Python/FastAPI for Section 1 and GitHub Actions for Section 2.

1. FastAPI app in `app/main.py`
2. Tests in `app/test_main.py`
3. Dockerfile in `app/Dockerfile` (with multi-stage + non-root user)
4. CI workflow in `.github/workflows/ci.yml`

The CI flow is: install deps → run flake8 → run pytest → build Docker image.

---

## How to run locally
From project root:

```bash
cd app
python3 -m pip install -r requirements.txt
python3 main.py
```

Then check endpoints:

```bash
curl http://localhost:8080/health
curl http://localhost:8080/version
curl http://localhost:8080/
```

---

## How to run tests
From project root:

```bash
cd app
python3 -m pytest test_main.py -v
```

These tests hit `/health`, `/version`, `/`, and one unknown route to confirm a 404.

---

## How to build and run Docker
From project root:

```bash
cd app
docker build -t assessment-app:latest .
docker run --rm -p 8080:8080 assessment-app:latest
```

In a second terminal:

```bash
curl http://localhost:8080/health
curl http://localhost:8080/version
curl http://localhost:8080/
```

---

## CI workflow explanation
Workflow file: `.github/workflows/ci.yml`

### What it does
- runs on push to `main`
- runs on PRs to `main`
- can run manually (`workflow_dispatch`)
- sets up Python 3.12
- installs dependencies
- runs flake8
- runs pytest
- builds the Docker image only if all previous steps pass

### How to trigger it
1. Push to `main`
2. Open PR to `main`
3. Or run manually in GitHub Actions tab

### If tests fail
GitHub marks the run as failed at the test step.
The Docker build step is skipped.

---

## Assumptions
- Python 3.11+ installed locally
- Docker is installed and running
- GitHub Actions runner is Linux (`ubuntu-latest`)
- app files stay under the `app/` folder

---

## What I learned
- how to add simple FastAPI routes quickly
- how to test API responses with `pytest` + `TestClient`
- how to build and run the same app locally and in Docker
- how to wire a basic CI pipeline in GitHub Actions

---

## What I would improve
- upload test artifacts for easier debugging
- add test coverage report in CI
- test multiple Python versions
- add image vulnerability scan
- push Docker image to a registry

---

## AI usage
I used AI for initial scaffolding and to clarify a few CI/CD concepts while building this.
I reviewed every file, ran tests and Docker locally, and manually changed code where needed.
