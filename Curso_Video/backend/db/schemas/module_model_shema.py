from db import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import uuid

class Module(Base):
    __tablename__ = 'modules' 

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    title = Column(String, nullable=False)  
    description = Column(String, nullable=True)
    
    course_id = Column(String(36), ForeignKey('courses.id'), nullable=False)  
    course = relationship('Course', backref='modules') 
    
    order = Column(Integer, nullable=False) 
