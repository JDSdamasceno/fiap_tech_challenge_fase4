from fastapi import FastAPI, HTTPException
from app.schemas import PredictRequest, PredictResponse
from app.service import ModelService
from app.config import settings
import time

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

model_service = ModelService(model_version=settings.MODEL_VERSION)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "api_version": settings.VERSION,
        "model_version": settings.MODEL_VERSION
    }


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    start_time = time.time()

    try:
        predictions = model_service.predict(
            historical_prices=request.historical_prices,
            horizon=request.horizon
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    latency_ms = int((time.time() - start_time) * 1000)

    return PredictResponse(
        predictions=predictions,
        horizon=request.horizon,
        model_version=settings.MODEL_VERSION
    )
