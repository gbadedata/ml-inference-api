from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_valid():
    payload = {"features": [0.1, 0.2, 0.3, 0.4]}
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "prediction" in data
    assert "probability" in data
    assert 0.0 <= data["probability"] <= 1.0

def test_predict_invalid_length():
    payload = {"features": [0.1, 0.2]}
    r = client.post("/predict", json=payload)
    assert r.status_code == 422