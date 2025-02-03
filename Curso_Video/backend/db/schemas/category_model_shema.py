from sqlalchemy import Column, String
from db import Base  
import uuid

class Category(Base):
    __tablename__ = 'categories'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)
