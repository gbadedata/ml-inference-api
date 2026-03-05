from typing import Annotated
from pydantic import BaseModel, Field, ConfigDict

Features4 = Annotated[
    list[float],
    Field(min_length=4, max_length=4, description="Exactly 4 numeric features.")
]

class PredictRequest(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    features: Features4

class PredictResponse(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    prediction: int
    probability: float
    model_version: str