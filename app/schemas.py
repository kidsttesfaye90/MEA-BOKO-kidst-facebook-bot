from pydantic import BaseModel, EmailStr, Field


class HealthResponse(BaseModel):
    status: str = Field(default="ok")
    service: str = Field(default="KIDMEA-BOKO")
    environment: str = Field(default="development")


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str


class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    is_active: bool
