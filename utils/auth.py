import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def create_token(user_id: int):
    """
    Create a token given a user id. 

    Args:
        user_id (int): User ID

    Returns:
        token: Token for user 
    """
    payload = {"user_id": user_id, "exp": datetime.utcnow() + timedelta(hours=1)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("user_id")
    except:
        return None
