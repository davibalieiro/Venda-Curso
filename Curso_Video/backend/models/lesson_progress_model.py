from pydantic import BaseModel
from typing import Optional
from user_model import User
from lesson_model import Lesson
from datetime import date

class CourseModel(BaseModel):
    id: str | None = None
    user: User
    lesson: Lesson
    watched: bool
    watched_at: str
    
    