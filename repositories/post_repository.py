from sqlalchemy.orm import Session
from models.post import Post

def create_post(db: Session, post: dict):
    db_post = Post(text=post["text"], user_id=post["user_id"])
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts_by_user(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def delete_post(db: Session, post_id: int):
    db.query(Post).filter(Post.id == post_id).delete()
    db.commit()
