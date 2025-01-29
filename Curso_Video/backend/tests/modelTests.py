
# tests/test_models.py
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.course_model import Course
from models.user_model import User
from models.module_model import Module
from models.lesson_model import Lesson
from models.enrollment_model import Enrollment
from models.review_model import Review
from models.category_model import Category

def mock_user():
    return User(id="1", name="Alice", email="alice@example.com", password="hashedpassword", role=["Student"], profile_picture=b"", bio="Learner", created_at="2025-01-01")

def mock_category():
    return Category(id="1", name="Programming", slug="programming")

def mock_course():
    return Course(id="1", title="Python Basics", description="Learn Python from scratch", instructor=mock_user(), price=100.0, category=mock_category(), level="Beginner", thumbnail="thumbnail.jpg", created_at="2025-01-01", updated_at="2025-01-02")

def mock_module():
    return Module(id="1", title="Introduction", description="Intro to Python", course=mock_course(), order="1")

def mock_lesson():
    return Lesson(id="1", title="Getting Started", description="First steps in Python", module=mock_module(), video_url="video.mp4", duration="10:00")

def mock_enrollment():
    return Enrollment(id="1", user=mock_user(), course=mock_course(), enrolled_at="2025-01-01", progress=0.0, completed=False)

def mock_review():
    return Review(id="1", user=mock_user(), course=mock_course(), rating=5, comment="Great course!", created_at="2025-01-02")

class TestModels(unittest.TestCase):
    def test_create_user(self):
        user = mock_user()
        self.assertEqual(user.name, "Alice")
        self.assertEqual(user.email, "alice@example.com")

    def test_create_category(self):
        category = mock_category()
        self.assertEqual(category.name, "Programming")

    def test_create_course(self):
        course = mock_course()
        self.assertEqual(course.title, "Python Basics")
        self.assertEqual(course.instructor.name, "Alice")

    def test_create_module(self):
        module = mock_module()
        self.assertEqual(module.title, "Introduction")
        self.assertEqual(module.course.title, "Python Basics")

    def test_create_lesson(self):
        lesson = mock_lesson()
        self.assertEqual(lesson.title, "Getting Started")
        self.assertEqual(lesson.video_url, "video.mp4")

    def test_create_enrollment(self):
        enrollment = mock_enrollment()
        self.assertEqual(enrollment.user.name, "Alice")
        self.assertFalse(enrollment.completed)

    def test_create_review(self):
        review = mock_review()
        self.assertEqual(review.user.name, "Alice")
        self.assertEqual(review.rating, 5)

if __name__ == "__main__":
    unittest.main()
