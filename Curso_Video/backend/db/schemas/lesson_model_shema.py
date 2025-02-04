from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
import uuid


class LessonSchema(Base):
    __tablename__ = 'lessons'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    module_id = Column(String(36), ForeignKey('modules.id'), nullable=False)
    module = relationship('Module', backref='lessons')

    video_url = Column(String, nullable=True)
    duration = Column(String, nullable=True)
