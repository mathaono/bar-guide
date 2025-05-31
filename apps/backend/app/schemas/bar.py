from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class BarCategory(str, Enum):
    bar_restaurante = "bar_restaurante"
    boteco = "boteco"
    bar_balada = "bar_balada"
    gastrobar = "gastrobar"
    bar_gamer = "bar_gamer"
    quiosque = "quiosque"
    hamburgueria = "hamburgueria"

class BarBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: BarCategory

    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    neighborhood: Optional[str] = None
    street: Optional[str] = None

class BarCreate(BarBase):
    pass

class BarResponse(BarBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True