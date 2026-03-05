# ML Inference API (FastAPI + Docker)

A containerised machine learning inference service built with:

-   Python 3.13
-   FastAPI
-   Pydantic v2
-   Docker
-   Docker Compose
-   pytest

This project demonstrates a production-style ML inference workflow
including:

-   deterministic model artifact generation
-   API-based prediction
-   strict request validation
-   structured JSON logging
-   environment configuration via .env
-   containerised deployment
-   automated endpoint tests

------------------------------------------------------------------------

# Architecture

Client ↓ FastAPI REST API ↓ Pydantic Request Validation ↓ Inference
Logic ↓ Model Artifact (model.json) ↓ Prediction Response

------------------------------------------------------------------------

# Project Structure

ml_inference_api

app/ main.py schemas.py config.py logging_conf.py model_loader.py

model/ train.py artifact/model.json

tests/ test_health.py test_predict.py

docs/evidence/

Dockerfile docker-compose.yml requirements.txt .env.example README.md

------------------------------------------------------------------------

# API Endpoints

## Health Check

GET /health

Response

{ "status": "ok" }

------------------------------------------------------------------------

## Version

GET /version

Response

{ "app": "ML Inference API", "version": "1.0.0" }

------------------------------------------------------------------------

## Prediction

POST /predict

Request

{ "features": \[0.1,0.2,0.3,0.4\] }

Rules

• exactly 4 numeric features • values must be floats

Response

{ "prediction": 1, "probability": 0.5411566681433093, "model_version":
"1.0.0" }

------------------------------------------------------------------------

# Local Setup

Create virtual environment

py -3.13 -m venv .venv

Activate

..venv`\Scripts`{=tex}`\Activate`{=tex}.ps1

Confirm

python --version

------------------------------------------------------------------------

# Install Dependencies

python -m pip install --upgrade pip python -m pip install -r
requirements.txt

Verify

python -m pip show fastapi

------------------------------------------------------------------------

# Generate Model Artifact

python model/train.py

This creates

model/artifact/model.json

------------------------------------------------------------------------

# Run API Locally

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

Open

http://localhost:8000/docs

Health

http://localhost:8000/health

------------------------------------------------------------------------

# Environment Variables

Copy template

cp .env.example .env

Variables

APP_NAME=ML Inference API APP_VERSION=1.0.0 LOG_LEVEL=INFO
MODEL_PATH=model/artifact/model.json

------------------------------------------------------------------------

# Running Tests

python -m pytest -q

Expected

2 passed

------------------------------------------------------------------------

# Docker

Build image

docker build -t ml-inference-api:1.0.0 .

Run container

docker run --rm -p 8000:8000 --env-file .env ml-inference-api:1.0.0

Open

http://localhost:8000/health http://localhost:8000/docs

Stop

CTRL + C

------------------------------------------------------------------------

# Docker Compose

Start

docker compose up

Stop

docker compose down

------------------------------------------------------------------------

# Troubleshooting

Port already in use

uvicorn app.main:app --port 8001

------------------------------------------------------------------------

Missing .env

Create from .env.example

------------------------------------------------------------------------

Missing model artifact

python model/train.py

------------------------------------------------------------------------

PowerShell curl alias

Use

curl.exe

Example

curl.exe -X POST "http://localhost:8000/predict" -H "Content-Type:
application/json" --data-raw "{\"features\":\[0.1,0.2,0.3,0.4\]}"

------------------------------------------------------------------------

# Evidence

All screenshots stored under

docs/evidence/

------------------------------------------------------------------------

# Final Verification

Local

python -m pip install -r requirements.txt python model/train.py uvicorn
app.main:app --reload python -m pytest -q

Container

docker build -t ml-inference-api:1.0.0 . docker run --rm -p 8000:8000
--env-file .env ml-inference-api:1.0.0

Compose

docker compose up

Health endpoint must return

{"status":"ok"}

Prediction endpoint must return valid response.
