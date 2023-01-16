from fastapi import FastAPI, Request, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sql_app import crud, model
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session


model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
    student_number: str
    password: str 
    user_name: str | None = None

class UserSignUp(BaseModel):
    user_name: str
    password: str 
    student_number: str | None = None


@app.get("/")
async def root():
    return {"message": "you are shakh"}

@app.post("/login/")
async def login(login_info:UserLogin, db: Session = Depends(get_db)):
    import json

    a = (login_info.json())
    a = json.loads(a)
    student_number = a['student_number']
    password = a['password']

    db_user = crud.get_user_by_student_num(db,  student_number)
    print(db_user)
    print(type(db_user))
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    #TODO
