from pydantic import BaseModel
from typing import Optional
from utils.schema_config import Schema

class ModuleSchema(Schema):
    title: str
    description: Optional[str]
    course_id: str
    order: int