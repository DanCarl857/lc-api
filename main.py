from fastapi import FastAPI, Depends
from controllers.auth_controller import signup, login
from controllers.post_controller import add_post, get_posts, delete_post
from schemas.user import UserCreate, UserLogin
from schemas.post import PostCreate
from dependencies import get_current_user, get_db

app = FastAPI()

@app.post("/signup")
def signup_endpoint(user: UserCreate, db=Depends(get_db)):
    return signup(user, db)

@app.post("/login")
def login_endpoint(user: UserLogin, db=Depends(get_db)):
    return login(user, db)

@app.post("/post")
def add_post_endpoint(post: PostCreate, user_id: int = Depends(get_current_user), db=Depends(get_db)):
    return add_post(post, user_id, db)

@app.get("/posts")
def get_posts_endpoint(user_id: int = Depends(get_current_user), db=Depends(get_db)):
    return get_posts(user_id, db)

@app.delete("/posts/{post_id}")
def delete_post_endpoint(post_id: int, user_id: int = Depends(get_current_user), db=Depends(get_db)):
    return delete_post(post_id, user_id, db)
