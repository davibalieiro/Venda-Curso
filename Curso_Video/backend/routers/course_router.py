from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import uuid4
from models.CourseModel import CourseModel
from db.fake_db import db

router = APIRouter(prefix="/course", tags=["Courses"])

@router.post('')
def create_course(course: CourseModel):
    if (course.name is None):
        return JSONResponse({
            'message': "the 'name' field don't be null",
            'data': None
        },
        status_code=400
    )
    if (course.price is None):
        return JSONResponse({
            'message': "the 'price' field don't be null",
            'data': None
        },
        status_code=400
    )
    course.id = str(uuid4())
    db.append(course.dict())
    
    return JSONResponse({
            'message': f"Course '{course.name}' created with price {course.price}",
            'data': course.dict()
        },
        status_code=201 
    )

@router.get('')
def get_course():
    return JSONResponse(
        {'message': 'success', 'data': db},
        status_code=200
    )

@router.delete('/{id}')
def delete_course(id: str):
    course = [c for c in db if c['id'] == id]
    if not course:
        return JSONResponse(
            {'message': f'Course with id {id} not found', 'data': None},
            status_code=404
        )
        
    db.remove(course[0])
    return JSONResponse(
        {'message': f'Course with id {id} deleted', 'data': None},
        status_code=200
    )
