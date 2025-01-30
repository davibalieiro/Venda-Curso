from pydantic import BaseModel
from typing import Optional
from datetime import date
from .user_model import User
from .category_model import Category

class Course(BaseModel):
    id: str | None = None
    title: str
    description: str
    instructor: User
    price: float
    category: Category 
    level: str # [Begginer, intermediary, advanced]
    thumbnail: bytes
    created_at: date
    updated_at: date 