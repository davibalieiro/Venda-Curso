from pydantic import BaseModel
from typing import Optional
from .module_model import Module

class Lesson(BaseModel):
    id: str | None = None
    title: str
    description: str
    module: Module
    video_url: str
    duration: str # Duration of the video

    