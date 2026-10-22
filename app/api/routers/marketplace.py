from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.crud.user import create_user, get_user_by_email
from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.core.dependencies import get_current_admin_user, get_current_user

router = APIRouter(prefix="/marketplace", tags=["marketplace"])


@router.get("/listings")
async def get_marketplace_listings(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return [{
        "id": 1,
        "title": "AI Automation package",
        "description": "Starter package for KIDMEA-BOKO operations",
        "price": 499.0,
        "category": "automation",
        "is_active": True,
    }]


@router.post("/listings", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_marketplace_listing(
    payload: dict,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user),
):
    return {"status": "created", "title": payload.get("title", "New listing"), "created_by": current_user.email}
