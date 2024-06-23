from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from api import users, sections, courses

app = FastAPI(
    title="Fastapi API LMS",
    description="LMS",
    version="0.0.1",
    contact={
        "name": "AnhKhOa",
        "email": "abc@gmail.com",

    },
    license_info={
        "name":"BKU"
    }
)



app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
