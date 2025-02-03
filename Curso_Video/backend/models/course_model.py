from pydantic import BaseModel
from typing import Optional
from datetime import date
from .user_model import UserSchema
from .category_model import CategorySchema
from Curso_Video.backend.utils.schema_config import Schema

class CourseSchema(Schema):
    
    title: str
    description: str
    instructor: UserSchema
    price: float
    category: CategorySchema
    level: str  # [Begginer, intermediary, advanced]
    thumbnail: str
    created_at: date
    updated_at: date