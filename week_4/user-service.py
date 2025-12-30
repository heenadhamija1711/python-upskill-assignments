from functools import wraps

import time
from functools import wraps

from week_4.admin import Admin


def requires_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not isinstance(user, Admin):
            raise PermissionError("Admin access required")
        return func(user, *args, **kwargs)
    return wrapper


def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

class UserService:

    @timed
    @requires_admin
    def delete_user(self, admin_user, user):
        print(f"{user.name} deleted by {admin_user.name}")
    def find_user(users, user_id):
        for user in users:
            if user.user_id == user_id:
                print("User found:", user)
                break
        else:
            print("User not found")
