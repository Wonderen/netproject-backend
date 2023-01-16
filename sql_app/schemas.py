from pydantic import BaseModel

class CommentBase(BaseModel):
    message: str
    owner_id: int

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    comment_id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    student_num: int

class UserCreate(UserBase):
    password: str
    username: str
    phone_num: int

class User(UserBase):
    student_num:int
    comments: list[Comment] = []

    class Config:
        orm_mode = True


