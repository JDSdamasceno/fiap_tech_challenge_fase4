from pydantic import BaseModel, Field, conlist
from typing import List, Optional


class PredictRequest(BaseModel):
    """
    Envie uma série histórica ordenada (mais antigo -> mais recente)
    """
    historical_prices: conlist(float, min_length=5) = Field(
        ...,
        description="Lista de preços históricos ordenados"
    )

    horizon: int = Field(
        5,
        ge=1,
        le=60,
        description="Quantidade de passos futuros a prever"
    )


class PredictResponse(BaseModel):
    predictions: List[float]
    horizon: int
    model_version: Optional[str] = None
