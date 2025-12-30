import time
from functools import wraps

def log_execution(enabled=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if enabled:
                print(f"[LOG] Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

class AuditService:

    @log_execution(enabled=True)
    def record(self, message):
        print(f"Audit: {message}")
