from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from repositories.post_repository import create_post, get_posts_by_user, delete_post
from schemas.post import PostCreate, PostResponse
from database import SessionLocal
from utils.cache import get_cached_posts, set_cached_posts

# Add a post
# Return a 400 code if the payload is too large > 1MB
def add_post(post: PostCreate, user_id: int, db: Session = Depends(SessionLocal)):
    if len(post.text.encode("utf-8")) > 1_000_000:  # 1 MB limit
        raise HTTPException(status_code=400, detail="Payload too large")
    new_post = create_post(db, {"text": post.text, "user_id": user_id})
    return {"post_id": new_post.id}

# Get all posts
# We try to get posts from the cache first and if there are no posts in the cache,
# then we get the posts fromt the database
# Posts gotten fromt the db are then saved in the cache
def get_posts(user_id: int, db: Session = Depends(SessionLocal)):
    cached_posts = get_cached_posts(user_id)
    if cached_posts:
        return cached_posts
    posts = get_posts_by_user(db, user_id)
    set_cached_posts(user_id, posts)
    return posts

# Delete a post given the POSTID
def delete_post(post_id: int, user_id: int, db: Session = Depends(SessionLocal)):
    delete_post(db, post_id)
    return {"message": "Post deleted"}
