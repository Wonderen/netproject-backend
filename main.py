from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = {'admin': 'admin', 'user1': '123'}

@app.get("/")
async def root():
    return {"message": "you are shakh"}

@app.post("/login/{user_name}/{password}")
async def login(user_name: str , password: str):
    if user_name in users.keys():
        if password == users[user_name]:
            return {"message": f"welcome {user_name}"}
        else:
            return {"message": "incorrect password"}
    else:
            return {"message": "not register"}
