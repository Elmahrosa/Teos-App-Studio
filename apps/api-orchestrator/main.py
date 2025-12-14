from fastapi import FastAPI
from routers import health

app = FastAPI(title="TEOS API Orchestrator")

# Routers
app.include_router(health.router)
