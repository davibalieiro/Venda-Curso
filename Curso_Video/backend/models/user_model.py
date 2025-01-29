from pydantic import BaseModel
from typing import Optional
from datetime import date

class User(BaseModel):
    id: str | None = None
    name: str
    email:str
    password: str # Hashed
    role: list[str]
    profile_picture: bytes
    bio:str
    created_at:date