from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.session import get_db
from app.integrations.registry import IntegrationRegistry

router = APIRouter(prefix="/integrations", tags=["integrations"])


@router.get("/available")
async def available_integrations(current_user=Depends(get_current_user)):
    return {
        "adapters": [
            "telegram",
            "gemini",
            "payment",
            "social",
            "fastbots",
        ],
    }


@router.get("/demo/{name}")
async def demo_integration(name: str, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    adapter = IntegrationRegistry.get_adapter(name)
    if name == "telegram":
        return adapter.send_message("12345", "demo message")
    if name == "gemini":
        return adapter.generate("hello KIDMEA-BOKO")
    if name == "payment":
        return adapter.charge(10.0)
    if name == "social":
        return adapter.publish("demo publish")
    if name == "fastbots":
        return adapter.trigger({"event": "demo"})
    return {"status": "unsupported"}
