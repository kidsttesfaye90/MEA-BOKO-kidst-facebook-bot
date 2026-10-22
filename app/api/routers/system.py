from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_admin_user, get_current_user
from app.db.session import get_db
from app.schemas.system import HealthResponse

router = APIRouter(tags=["system"])


@router.get("/health", response_model=HealthResponse)
async def health(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        db_ok = "ok"
    except Exception:
        db_ok = "unavailable"
    return {"status": "ok", "service": "KIDMEA-BOKO", "database": db_ok}


@router.get("/system/info")
async def system_info(current_user=Depends(get_current_user)):
    return {
        "app_name": "KIDMEA-BOKO",
        "version": "0.1.0",
        "environment": "development",
        "user": current_user.email,
    }


@router.get("/system/admin")
async def admin_only(current_user=Depends(get_current_admin_user)):
    return {"status": "ok", "message": f"admin access granted to {current_user.email}"}
