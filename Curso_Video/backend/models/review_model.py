from pydantic import BaseModel
from .user_model import User
from .course_model import Course
from datetime import date


class Review(BaseModel):
    id: str | None = None
    user: User
    course: Course
    rating: int # from 1 to 5
    comment: str
    created_at: str
    