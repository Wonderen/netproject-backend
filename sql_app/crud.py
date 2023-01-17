from sqlalchemy.orm import Session
from . import model, schemas
from utils.hash import make_hash

def get_user_by_student_num(db: Session, student_num: int):
    return db.query(model.User).filter(model.User.student_num == student_num).first()

def get_user_by_email(db: Session, user_email: str):
    return db.query(model.User).filter(model.User.user_email == user_email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserSignUp):
    fake_hashed_password = make_hash(user.password)
    db_user = model.User(student_num = user.student_number, user_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_comment(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Comment).offset(skip).limit(limit).all()

def create_user_comment(db: Session, comment: schemas.CommentCreate, student_num: int):
    db_comment = model.Comment(**comment.dict(), owner_id=student_num)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment