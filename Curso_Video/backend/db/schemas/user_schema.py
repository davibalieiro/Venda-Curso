from db import Base
from sqlalchemy import Column, String, Date, Boolean, func
import uuid

DEFAULT_PICTURE_URL = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png'

class User(Base):
    __tablename__ = 'users'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default='student') 
    profile_picture = Column(String, default=DEFAULT_PICTURE_URL)
    bio = Column(String, nullable=True)
    
    created_at = Column(Date, default=func.now())  
    is_active = Column(Boolean, nullable=False, default=True)  
