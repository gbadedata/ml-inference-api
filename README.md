# ML Inference API (FastAPI + Docker)

A containerised machine learning inference service built with:

-   Python 3.13
-   FastAPI
-   Pydantic v2
-   Docker
-   Docker Compose
-   pytest

This project demonstrates a production‑style ML inference workflow
including:

-   deterministic model artifact generation
-   API-based prediction
-   strict request validation
-   structured JSON logging
-   environment configuration via `.env`
-   containerised deployment
-   automated endpoint tests

------------------------------------------------------------------------

# Architecture

Client → FastAPI REST API → Pydantic Request Validation → Inference
Logic → Model Artifact (`model.json`) → Prediction Response

------------------------------------------------------------------------

# Project Structure

    ml_inference_api/
    │
    ├─ app/
    │   ├─ main.py
    │   ├─ schemas.py
    │   ├─ config.py
    │   ├─ logging_conf.py
    │   └─ model_loader.py
    │
    ├─ model/
    │   ├─ train.py
    │   └─ artifact/
    │
    ├─ tests/
    │   ├─ test_health.py
    │   └─ test_predict.py
    │
    ├─ docs/
    │   └─ evidence/
    │
    ├─ .env.example
    ├─ Dockerfile
    ├─ docker-compose.yml
    ├─ requirements.txt
    └─ README.md

------------------------------------------------------------------------

# API Endpoints

## Health

    GET /health

Response

``` json
{
  "status": "ok"
}
```

------------------------------------------------------------------------

## Version

    GET /version

Response

``` json
{
  "app": "ML Inference API",
  "version": "1.0.0"
}
```

------------------------------------------------------------------------

## Predict

    POST /predict

Example request

``` json
{
  "features": [0.1, 0.2, 0.3, 0.4]
}
```

Example response

``` json
{
  "prediction": 1,
  "probability": 0.54,
  "model_version": "1.0.0"
}
```

------------------------------------------------------------------------

# Local Setup

### Create virtual environment

    py -3.13 -m venv .venv

Activate

    .\.venv\Scripts\Activate.ps1

------------------------------------------------------------------------

### Install dependencies

    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

------------------------------------------------------------------------

### Train model artifact

    python model/train.py

Creates

    model/artifact/model.json

------------------------------------------------------------------------

### Run API

    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

Open

    http://localhost:8000/health
    http://localhost:8000/docs

------------------------------------------------------------------------

# Environment Variables

Create `.env` from `.env.example`

  Variable      Description
  ------------- ------------------------
  APP_NAME      API display name
  APP_VERSION   API version
  LOG_LEVEL     Logging level
  MODEL_PATH    Path to model artifact

Example

    APP_NAME=ML Inference API
    APP_VERSION=1.0.0
    LOG_LEVEL=INFO
    MODEL_PATH=model/artifact/model.json

------------------------------------------------------------------------

# Running Tests

    python -m pytest -q

Tests validate

-   health endpoint
-   valid prediction
-   invalid prediction input

------------------------------------------------------------------------

# Docker

Build image

    docker build -t ml-inference-api:1.0.0 .

Run container

    docker run --rm -p 8000:8000 --env-file .env ml-inference-api:1.0.0

------------------------------------------------------------------------

# Docker Compose

Start

    docker compose up

Stop

    docker compose down

------------------------------------------------------------------------

# Sending Requests from PowerShell (Important)

PowerShell sometimes corrupts JSON when using curl.\
The safest method is sending JSON from a file.

### Step 1 --- Create payload

    Set-Content -Path payload.json -Value '{ "features": [0.1, 0.2, 0.3, 0.4] }' -Encoding utf8

### Step 2 --- Send request

    curl.exe -v -H "Content-Type: application/json" --data-binary "@payload.json" "http://localhost:8000/predict"

Expected response

``` json
{
  "prediction": 1,
  "probability": 0.54,
  "model_version": "1.0.0"
}
```

------------------------------------------------------------------------

# Clean‑up Rule

Do **not commit payload.json**.

Add to `.gitignore`

    payload.json

------------------------------------------------------------------------

# Troubleshooting

### Port already in use

    netstat -ano | findstr :8000

### Model file missing

    python model/train.py

### Missing `.env`

Copy

    .env.example → .env

### PowerShell curl alias

PowerShell aliases curl to another command.

Always use

    curl.exe

instead of

    curl

------------------------------------------------------------------------

# Project Goal

This repository demonstrates a **containerised production‑style ML
inference service** including:

-   API validation
-   environment configuration
-   automated tests
-   Docker containerisation
-   Docker Compose orchestration

Foundation for

-   CI/CD pipelines
-   container registry publishing
-   Kubernetes deployment
-   monitoring with Prometheus
