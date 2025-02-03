from sqlalchemy import Column, String, Date, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base  
from datetime import datetime
import uuid

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='enrollments')
    
    course_id = Column(String(36), ForeignKey('courses.id'), nullable=False)
    course = relationship('Course', backref='enrollments')
    
    enrolled_at = Column(Date, default=datetime.utcnow)
    progress = Column(Float, nullable=False, default=0.0)
    completed = Column(Boolean, nullable=False, default=False) 
