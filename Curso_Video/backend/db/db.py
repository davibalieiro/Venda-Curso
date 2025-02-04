from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

db = create_engine('sqlite:///course.db')

Base.metadata.create_all(bind=db)

# Create a session
Session = sessionmaker(bind=db)
session = Session()
