from pydantic import BaseModel

class CommentBase(BaseModel):
    message: str
    owner_id: int

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    comment_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    student_num: int

class UserSignUp(BaseModel):
    user_name: str
    student_number: str
    phone_number: str
    password: str

class UserLogin(BaseModel):
    student_number: str
    password: str 
    user_name: str | None = None

class User(UserBase):
    student_num:int
    comments: list[Comment] = []

    class Config:
        orm_mode = True


