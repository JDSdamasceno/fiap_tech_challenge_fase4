# README.md — Tech Challenge Stock Forecast API (FastAPI)
# Objetivo: rodar e testar a API /health e /predict (predição mockada)

# =========================
# 1) Rodar local (sem Docker)
# =========================
# # (opcional) criar venv
# Windows PowerShell:
#   python -m venv .venv
#   .\.venv\Scripts\Activate.ps1
# Windows CMD:
#   python -m venv .venv
#   .\.venv\Scripts\activate.bat
# Linux/Mac:
#   python3 -m venv .venv
#   source .venv/bin/activate

# instalar dependências
#   pip install -r requirements.txt

# subir a API (na raiz do projeto)
#   uvicorn app.main:app --reload

# a API ficará em:
#   http://localhost:8000

# =========================
# 2) Testar via Swagger (mais fácil)
# =========================
# abrir:
#   http://localhost:8000/docs
# testar:
#   POST /predict -> Try it out -> cole o JSON abaixo -> Execute
#   {
#     "historical_prices": [10.0, 10.2, 10.5, 10.7, 10.9],
#     "horizon": 5
#   }


# =========================
# 3) Testar endpoints (curl)
# =========================
# healthcheck
# Windows / Linux / Mac:
#   curl http://localhost:8000/health

# predict (Windows CMD/PowerShell)
#   curl -X POST "http://localhost:8000/predict" ^
#     -H "Content-Type: application/json" ^
#     -d "{\"historical_prices\":[10.0,10.2,10.5,10.7,10.9],\"horizon\":5}"

# predict (Linux/Mac)
#   curl -X POST "http://localhost:8000/predict" \
#     -H "Content-Type: application/json" \
#     -d '{
#       "historical_prices": [10.0, 10.2, 10.5, 10.7, 10.9],
#       "horizon": 5
#     }'

# =========================
# 4) Testar via Python (requests)
# =========================
# crie um arquivo test_request.py com:
#   import requests
#   url = "http://localhost:8000/predict"
#   payload = {"historical_prices":[10.0,10.2,10.5,10.7,10.9], "horizon": 5}
#   r = requests.post(url, json=payload)
#   print(r.status_code, r.json())
# rode:
#   python test_request.py

# =========================
# 5) Rodar com Docker
# =========================
# build:
#   docker build -t tc-api .
# run:
#   docker run -p 8000:8000 tc-api
# testar:
#   http://localhost:8000/docs

# =========================
# 6) Onde plugar o modelo real
# =========================
# Substitua a lógica mock em:
#   app/service.py -> ModelService.predict(historical_prices, horizon)
# Retorne uma List[float] com tamanho = horizon
