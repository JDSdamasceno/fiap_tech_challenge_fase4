from typing import List
import numpy as np
import joblib
from tensorflow import keras


class ModelService:
    """
    Serviço responsável por carregar e chamar o modelo treinado.
    """

    def __init__(
        self,
        model_path: str = "artifacts/model.keras",
        scaler_path: str = "artifacts/scaler.pkl",
        model_version: str = "v1"
    ):
        self.model_version = model_version

        # Carrega modelo e scaler uma única vez
        self.model = keras.models.load_model(model_path)
        self.scaler = joblib.load(scaler_path)

    def predict(self, historical_prices: List[float], horizon: int) -> List[float]:
        """
        Recebe série histórica e retorna previsões futuras.
        """
        series = np.array(historical_prices, dtype=np.float32)

        predictions = []
        working_series = series.copy()

        window_size = 60  # ⚠️ deve ser igual ao usado no treino

        for _ in range(horizon):

            # 1️⃣ pegar últimos valores da janela
            window = working_series[-window_size:]

            # 2️⃣ reshape para modelo (1, window_size, 1)
            window = window.reshape(-1, 1)
            window_scaled = self.scaler.transform(window)
            X = window_scaled.reshape(1, window_size, 1)

            # 3️⃣ prever próximo passo
            y_scaled = self.model.predict(X, verbose=0)

            # 4️⃣ voltar para escala original
            y_pred = self.scaler.inverse_transform(y_scaled)[0][0]

            predictions.append(float(y_pred))

            # 5️⃣ adicionar previsão na série para próximo loop
            working_series = np.append(working_series, y_pred)

        return predictions
