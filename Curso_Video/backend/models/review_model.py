from pydantic import BaseModel
from .user_model import UserSchema
from .course_model import CourseSchema
from datetime import date
from utils.schema_config import Schema

class ReviewSchema(Schema):
    user: UserSchema
    course: CourseSchema
    rating: int 
    comment: str
    created_at: date