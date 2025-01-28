from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()
db: List[dict] = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class CourseModel(BaseModel):
    id: str | None = None
    name: str
    price: float

@app.post('/course')
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

@app.get('/course')
def get_course():
    return JSONResponse(
        {'message': 'success', 'data': db},
        status_code=200
    )

@app.delete('/course/{id}')
def delete_course(id: str):
    for course in db:
        if course['id'] == id:
            db.remove(course)
            return JSONResponse(
                {'message': f'Course {id} deleted successfully', 'data': db},
                status_code=200
            )
    return JSONResponse(
        {'message': f'Course {id} not found', 'data': db},
        status_code=404
    )