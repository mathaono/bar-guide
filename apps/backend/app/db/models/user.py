from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from typing import Optional
from app.db.db import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_pass: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    nickname: Mapped[str] = mapped_column(String(255), nullable=False)

    cpf: Mapped[Optional[str]] = mapped_column(String(14), nullable=True)
    cell: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)

    country: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    state: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    neighborhood: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    street: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)