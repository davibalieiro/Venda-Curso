from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class User(BaseModel):
    id: str | None = None
    name: str
    email:str
    password: str # Hashed
    role: List[str]
    profile_picture: str
    bio:str
    created_at: str