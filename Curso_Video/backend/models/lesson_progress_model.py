from pydantic import BaseModel
from typing import Optional
from datetime import date
from Curso_Video.backend.utils.schema_config import Schema

class LessonProgressSchema(Schema):
    user_id: str
    lesson_id: str
    watched: bool
    watched_at: Optional[date]