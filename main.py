from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

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


users = []

class User(BaseModel):
    email:str
    is_active: bool
    bio: Optional[str]

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/users")
async def create_user(user:User):
    users.append(user)
    return "Successfully created User"

@app.get("users/{id}")
async def get_user(
    id:int = Path(..., description="The ID of the user you want to retrieve.",gt=2),
                   
                   q: str = Query(None, max_length=5)
                   ):
    
    return {"users": users[id], "query": q}

