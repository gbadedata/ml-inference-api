from pathlib import Path
import json

ARTIFACT_DIR = Path(__file__).resolve().parent / "artifact"
MODEL_PATH = ARTIFACT_DIR / "model.json"

def main() -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

    model = {
        "type": "linear_threshold",
        "weights": [1.0, 0.5, -0.25, 0.1],
        "bias": 0.0,
        "threshold": 0.0,
        "version": "1.0.0"
    }

    MODEL_PATH.write_text(json.dumps(model, indent=2), encoding="utf-8")
    print(f"Saved model to: {MODEL_PATH}")

if __name__ == "__main__":
    main()