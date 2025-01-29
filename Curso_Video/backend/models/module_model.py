from pydantic import BaseModel
from typing import Optional
from .course_model import Course

class Module(BaseModel):
    id: str | None = None
    title: str
    description:str
    course: Course
    order: int 
    