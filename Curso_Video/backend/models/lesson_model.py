from pydantic import BaseModel
from typing import Optional
from Curso_Video.backend.utils.schema_config import Schema

class LessonSchema(Schema):
    title: str
    description: Optional[str]
    module_id: str
    video_url: Optional[str]
    duration: Optional[str]

    