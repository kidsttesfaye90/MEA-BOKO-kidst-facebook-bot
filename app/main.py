from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings

app = FastAPI(
    title="KIDMEA-BOKO",
    version="0.1.0",
    description="General digital market, B2B brokerage, and business services platform.",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.cors_origins.split(",") if origin.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "KIDMEA-BOKO",
        "environment": settings.environment,
    }


@app.get("/api/v1/health")
async def api_v1_health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "KIDMEA-BOKO",
        "environment": settings.environment,
    }
