from pydantic import BaseModel
from typing import Optional


class Schema(BaseModel):
    id: Optional[str] = None

    class Config:
        from_attributes = True