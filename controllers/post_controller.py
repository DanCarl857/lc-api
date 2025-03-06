from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from repositories.post_repository import create_post, get_posts_by_user, delete_post
from schemas.post import PostCreate, PostResponse
from database import SessionLocal
from utils.cache import get_cached_posts, set_cached_posts

def add_post(post: PostCreate, user_id: int, db: Session = Depends(SessionLocal)):
    """
    Create a new post. 

    Args:
        post (PostCreate): Post text 

    Returns:
        post_id: Newly created post id

    Raises:
        error (400): Payload too large if payload is > 1M 
    """
    if len(post.text.encode("utf-8")) > 1_000_000:  # 1 MB limit
        raise HTTPException(status_code=400, detail="Payload too large")
    new_post = create_post(db, {"text": post.text, "user_id": user_id})

    # Once we create a post we need to make sure the cache is updated
    posts = get_posts_by_user(db, user_id)
    set_cached_posts(user_id, posts)

    # return the post_id we just created
    return {"post_id": new_post.id}

def get_posts(user_id: int, db: Session = Depends(SessionLocal)):
    """
    Get all posts.

    Args:
        user_id (int): user id,
        db (Session): DB session

    Returns:
        posts: All user's posts 
    """
    # first check the cache for posts
    cached_posts = get_cached_posts(user_id)
    if cached_posts:
        return cached_posts

    # Update the cache with all posts in the database
    posts = get_posts_by_user(db, user_id)
    set_cached_posts(user_id, posts)
    
    return posts

def delete_post(post_id: int, user_id: int, db: Session = Depends(SessionLocal)):
    """
    Delete a post given an id.

    Args:
        post_id (int): Post ID to be deleted 

    Returns:
        post_id: Post ID of the post to be deleted. 
    """
    delete_post(db, post_id)
    return {"message": "Post deleted"}
