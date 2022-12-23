from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "localhost",
    "http://localhost",
    "http://192.168.1.34",
    "http://localhost:8000",
    "localhost:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = {'admin': 'admin', 'user1': '123'}

class UserLogin(BaseModel):
    user_name: str
    password: str 
    student_number: str | None = None


@app.get("/")
async def root():
    return {"message": "you are shakh"}

@app.post("/login/")
async def login(login_info:Request):
    a = (await login_info.json())
    print(a)
    user_name = a['user_name']
    password = a['password']
    if user_name in users.keys():
        if password == users[user_name]:
            return {"message": f"welcome {user_name}"}
        else:
            return {"message": "incorrect password"}
    else:
            return {"message": "not register"}
