from pydantic import BaseModel
from .user_model import UserSchema
from .course_model import CourseSchema
from datetime import date
from Curso_Video.backend.utils.schema_config import Schema

class EnrollmentShema(Schema):
    user: UserSchema
    course: CourseSchema
    enrolled_at: date
    progress: float
    completed: bool 
