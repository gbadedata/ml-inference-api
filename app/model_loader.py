import json
from pathlib import Path
import logging

logger = logging.getLogger("app")

def load_model(model_path: str) -> dict:
    path = Path(model_path)
    if not path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")
    model = json.loads(path.read_text(encoding="utf-8"))
    logger.info(f"Loaded model from {model_path}")
    return model

def predict_linear_threshold(model: dict, features: list[float]) -> tuple[int, float]:
    w = model["weights"]
    b = model["bias"]
    t = model["threshold"]

    score = sum(features[i] * w[i] for i in range(4)) + b
    prob = 1.0 / (1.0 + (2.718281828 ** (-score)))
    pred = int(score >= t)
    return pred, float(prob)