from pydantic import BaseModel
from typing import Optional

class CourseModel(BaseModel):
    id: str | None = None
    name: str
    price: float