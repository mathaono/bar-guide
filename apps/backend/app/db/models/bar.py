from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from geoalchemy2 import Geometry
from datetime import datetime
from enum import Enum as PyEnum
from typing import Optional
from app.db.db import Base

class BarCategory(PyEnum):
    BAR_RESTAURANTE = "bar_restaurante"
    BOTECO = "boteco"
    BAR_BAlADA = "bar_balada"
    GASTROBAR = "gastrobar"
    BAR_GAMER = "bar_gamer"
    QUIOSQUE = "quiosque"
    HAMBURGUERIA = "hamburgueria"


class Bar(Base):
    __tablename__ = "bars"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    category: Mapped[str] = mapped_column(String(50), nullable=False)

    location: Mapped[str] = mapped_column(Geometry(geometry_type="POINT", srid=4326), nullable=False)

    country: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    state: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    neighborhood: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    street: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    created_by: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)