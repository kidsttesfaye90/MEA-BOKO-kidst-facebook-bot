from pydantic import BaseModel, ConfigDict, Field


class MarketplaceItemBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    description: str | None = None
    price: float | None = None
    category: str = "general"


class MarketplaceItemCreate(MarketplaceItemBase):
    pass


class MarketplaceItemResponse(MarketplaceItemBase):
    id: int
    is_active: bool
