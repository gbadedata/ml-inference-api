from fastapi import FastAPI, HTTPException
import logging
from app.config import settings
from app.logging_conf import configure_logging
from app.schemas import PredictRequest, PredictResponse
from app.model_loader import load_model, predict_linear_threshold

configure_logging(settings.log_level)
logger = logging.getLogger("app")

app = FastAPI(title=settings.app_name, version=settings.app_version)

try:
    MODEL = load_model(settings.model_path)
except Exception as e:
    logger.error(f"Startup failed: {e}")
    MODEL = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"app": settings.app_name, "version": settings.app_version}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    if MODEL is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    try:
        pred, prob = predict_linear_threshold(MODEL, req.features)
        return PredictResponse(
            prediction=pred,
            probability=prob,
            model_version=settings.app_version,
        )
    except Exception as e:
        logger.error(f"Predict error: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")