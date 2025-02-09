from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate


# CREATE
def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


# READ
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, offset: int = 0, limit: int = 100):
    return db.query(User).offset(offset).limit(limit).all()


# UPDATE
def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for key, value in user.model_dump().items():
            setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)


# DELETE
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False
