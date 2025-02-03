from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from Curso_Video.backend.utils.schema_config import Schema


class UserSchema(Schema):
    name: str
    email: str
    password: str  # Hashed
    role: List[str]
    profile_picture: str
    bio: str
    created_at: date
