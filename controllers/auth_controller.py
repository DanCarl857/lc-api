from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from repositories.user_repository import get_user_by_email, create_user
from schemas.user import UserCreate, UserLogin, Token
from database import SessionLocal
from utils.auth import create_token

# Signup user given a unique email and password
# Return 400 code if user is already registered
def signup(user: UserCreate, db: Session = Depends(SessionLocal)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = create_user(db, user.dict())
    token = create_token(new_user.id)
    return Token(token=token)

# Login user given their login and password
# Return 400 error code if credentials are invalid
def login(user: UserLogin, db: Session = Depends(SessionLocal)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_token(db_user.id)
    return Token(token=token)
