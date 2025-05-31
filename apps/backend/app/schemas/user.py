from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class Address(BaseModel):
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    neighborhood: Optional[str] = None
    street: Optional[str] = None

class UserBase(BaseModel):
        name: str
        nickname: str
        email: EmailStr
        address: Optional[Address] = None

class UserCreate(UserBase):
      pass_: str

class UserResponse(UserBase):
      id: int
      created_at: datetime

      class Config:
            orm_mode = True