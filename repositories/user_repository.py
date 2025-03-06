from sqlalchemy.orm import Session
from models.user import User

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: dict):
    db_user = User(email=user["email"], password=user["password"])
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
