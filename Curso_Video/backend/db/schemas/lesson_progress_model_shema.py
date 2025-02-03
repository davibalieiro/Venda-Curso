from sqlalchemy import Column, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime
import uuid

class LessonProgress(Base):
    __tablename__ = 'lesson_progress'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='lesson_progress')
    
    lesson_id = Column(String(36), ForeignKey('lessons.id'), nullable=False)
    lesson = relationship('Lesson', backref='progress')
    
    watched = Column(Boolean, nullable=False, default=False)
    watched_at = Column(Date, nullable=True)  
