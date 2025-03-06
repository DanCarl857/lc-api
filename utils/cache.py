from datetime import datetime, timedelta

cache = {}

def get_cached_posts(user_id: int):
    """
    Get Cached Posts - gets all the posts we have cached. 

    Args:
        user_id (int): User ID whose posts we need from the cache

    Returns:
        posts: All the user's posts in the cache

    Also returns None if there are not posts in the cache
    """
    if user_id in cache and datetime.now() < cache[user_id]["expiry"]:
        return cache[user_id]["posts"]
    return None

def set_cached_posts(user_id: int, posts):
    """
    Set cached posts - Add posts for a user into the cache.

    Args:
        user_id (int): User ID whose posts we need from the cache
        posts (Posts): Posts we want to add into the cache for said user

    Returns:
        posts: All the user's posts in the cache
    """
    cache[user_id] = {"posts": posts, "expiry": datetime.now() + timedelta(minutes=5)}
