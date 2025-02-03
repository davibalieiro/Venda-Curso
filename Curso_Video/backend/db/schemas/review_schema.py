from db import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, func
from sqlalchemy.orm import relationship
import uuid


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(String(36), primary_key=True, default=lambda: str(
        uuid.uuid4()), unique=True, index=True)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    course_id = Column(String(36), ForeignKey('courses.id'), nullable=False)

    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    created_at = Column(Date, default=func.now())

    user = relationship('User', backref='reviews')
    course = relationship('Course', backref='reviews')
