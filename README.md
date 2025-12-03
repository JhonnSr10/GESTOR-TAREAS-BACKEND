# backend_fastapi

Proyecto backend para el Gestor de Tareas usando FastAPI y PostgreSQL.

Requisitos:
- Docker y Docker Compose (recomendado)
- Python 3.11 (si ejecutas localmente)

Comandos (PowerShell):

# Usando Docker Compose
docker-compose up --build

# Ejecutar localmente (sin Docker, en Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

La API estará disponible en `http://localhost:8000`.
