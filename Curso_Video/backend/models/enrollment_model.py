from pydantic import BaseModel
from .user_model import User
from .course_model import Course
from datetime import date

class Enrollment(BaseModel):
    id: str | None = None
    user: User
    course: Course
    enrolled_at: str
    progress: float # in percentage, shows the progress of the course
    completed: bool # if progress != 100, its false
    