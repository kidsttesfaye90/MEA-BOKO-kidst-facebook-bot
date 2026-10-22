from pydantic import BaseModel, ConfigDict, EmailStr


class SystemStatus(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    app_name: str
    version: str
    environment: str
    database: str


class HealthResponse(BaseModel):
    status: str
    service: str
    database: str
