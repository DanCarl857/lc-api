from datetime import datetime, timedelta

cache = {}

def get_cached_posts(user_id: int):
    if user_id in cache and datetime.now() < cache[user_id]["expiry"]:
        return cache[user_id]["posts"]
    return None

def set_cached_posts(user_id: int, posts):
    cache[user_id] = {"posts": posts, "expiry": datetime.now() + timedelta(minutes=5)}
