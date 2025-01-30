from fastapi import APIRouter
from uuid import uuid4
from db.fake_db import db
from models.course_model import Course
from utils.responses import response

router = APIRouter(prefix="/course", tags=["Courses"])



@router.post('')
def create_course(course: Course):
    for field in ["title", "price"]:
        if not getattr(course, field):
            return response(f"The '{field}' field can't be null", status=400)

    course.id = str(uuid4())
    db.append(course.dict())
    return response(f"Course '{course.title}' created with price {course.price}", course.dict(), 201)

@router.get('')
def get_course():
    return response('success', db)

@router.delete('/{id}')
def delete_course(id: str):
    course = next((c for c in db if c['id'] == id), None)
    if not course:
        return response(f'Course with id {id} not found', status=404)

    db.remove(course)
    return response(f'Course with id {id} deleted')
