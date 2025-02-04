
import unittest
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from uuid import uuid4
import sys
import os

try:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    from db import Base
    from db.schemas.course_model_shema import CourseSchema, CourseLevel
    from db.schemas import User
except Exception as e:
    print(e)



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
        teacher = User(
            id=str(uuid4()),
            name='José Felicidade',
            email='email@example.com',
            password='JoseSenha',
            role='teacher',
            bio='A good bio',
        )

        course = CourseSchema(
            id=str(uuid4()),
            title='Test Course',
            description='This is a test course',
            instructor_id=str(teacher.id),
            price=99.99,
            category='Programming',
            level=CourseLevel.beginner,
            thumbnail='http://example.com/thumbnail.jpg'
        )
        self.session.add(course)
        self.session.commit()

        retrieved_course = self.session.query(
            CourseSchema).filter_by(id=course.id).one()
        self.assertEqual(retrieved_course.title, 'Test Course')
        self.assertEqual(retrieved_course.description, 'This is a test course')
        self.assertEqual(retrieved_course.price, 99.99)
        self.assertEqual(retrieved_course.category, 'Programming')
        self.assertEqual(retrieved_course.level, CourseLevel.beginner)
        self.assertEqual(retrieved_course.thumbnail,
                         'http://example.com/thumbnail.jpg')


if __name__ == '__main__':
    unittest.main()
