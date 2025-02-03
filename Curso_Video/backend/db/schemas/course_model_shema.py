from sqlalchemy import Column, String, Date, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime
import uuid
import enum

class CourseLevel(enum.Enum):
    beginner = "Beginner"
    intermediary = "Intermediary"
    advanced = "Advanced"

class CourseSchema(Base):
    __tablename__ = 'courses'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    instructor_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    instructor = relationship('UserSchema', backref='courses')
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    level = Column(Enum(CourseLevel), nullable=False)
    thumbnail = Column(String, nullable=False)    
    created_at = Column(Date, default=datetime.utcnow)
    updated_at = Column(Date, default=datetime.utcnow, onupdate=datetime.utcnow)
