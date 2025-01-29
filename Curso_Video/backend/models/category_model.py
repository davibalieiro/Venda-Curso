from pydantic import BaseModel

class Category(BaseModel):
    id: str | None = None
    name: str
    slug: str