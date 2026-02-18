from typing import List
import random


class ModelService:
    """
    Serviço responsável por chamar o modelo.
    Neste momento está mockado.
    """

    def __init__(self, model_version: str = "v1"):
        self.model_version = model_version

    def predict(self, historical_prices: List[float], horizon: int) -> List[float]:
        """
        Substitua essa lógica pela chamada real do seu modelo.
        """
        last_price = historical_prices[-1]

        # Simulação simples (mock)
        predictions = []
        for _ in range(horizon):
            variation = random.uniform(-0.5, 0.5)
            next_price = round(last_price + variation, 2)
            predictions.append(next_price)
            last_price = next_price

        return predictions
