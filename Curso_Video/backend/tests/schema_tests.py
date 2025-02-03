import unittest
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from uuid import uuid4

try:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from db.schemas.course_model_shema import CourseSchema
    from db import Base
except ImportError as e:
    print(f"ImportError: {e}")
    raise

class TestCourseModelSchema(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)
        cls.engine.dispose()

    def setUp(self):
        self.session = self.Session()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_create_course(self):
        course = CourseSchema(
            id=str(uuid4()),
            title='Test Course',
            description='This is a test course',
            instructor_id=str(uuid4()),
            price=99.99,
            category='Programming',
            level='Beginner',
            thumbnail='http://example.com/thumbnail.jpg',
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        self.session.add(course)
        self.session.commit()

        retrieved_course = self.session.query(
            CourseSchema).filter_by(id=course.id).one()
        self.assertEqual(retrieved_course.title, 'Test Course')
        self.assertEqual(retrieved_course.description, 'This is a test course')
        self.assertEqual(retrieved_course.price, 99.99)
        self.assertEqual(retrieved_course.category, 'Programming')
        self.assertEqual(retrieved_course.level, 'Beginner')
        self.assertEqual(retrieved_course.thumbnail,
                         'http://example.com/thumbnail.jpg')


if __name__ == '__main__':
    unittest.main()
