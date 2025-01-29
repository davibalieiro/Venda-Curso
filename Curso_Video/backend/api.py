from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.course_router import router as course_router
from middleware.cors_config import add_cors_middleware

app = FastAPI()
app.include_router(course_router)
add_cors_middleware(app)


@app.get("/")
def root():
    return {"message": "Welcome to the API"}


    