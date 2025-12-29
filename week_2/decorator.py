# 1. Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the start and end time. Calculate the total time taken and print.
#
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Total time taken: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def append_numbers():
    numbers = []
    for i in range(1, 1001):
        numbers.append(i)
    return numbers

append_numbers()

# 2. Create a parameterised decorator retry that retries a function a specified number of times.
#
# @retry(3)
# def may_fail(name):
#     print(f"Hello, {name}!")

import random
import time


def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print(f"Attempt {attempt} failed: {e}")
                    time.sleep(0.5)  # optional delay between retries
            print(f"All {times} attempts failed.")
        return wrapper
    return decorator


@retry(3)
def may_fail(name):
    if random.random() < 0.5:  # simulate a failure 50% of the time
        raise ValueError("Random failure!")
    print(f"Hello, {name}!")

# Test the function
may_fail("Alice")


# 3. Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.
#
# def square_root(x):
#     return x ** 0.5
#


def validate_positive(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("Argument must be positive")
        return func(x)
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5

print(square_root(16))

#
# 4. Create a decorator cache that caches the result of a function based on its arguments.
# @cache
# def expensive_computation(x):
#     print("Performing computation...")
#     return x * x
#
# expensive_computation(5)
# expensive_computation(5)
#
# Write a cache decorator for it to check if the calculation is already performed then return the result.
#

# Decorator to cache function results

def cache(func):
    memo = {}

    def wrapper(*args):
        if args in memo:
            print("Returning cached result...")
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result

    return wrapper

@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x

print(expensive_computation(5))
print(expensive_computation(5))
print(expensive_computation(6))
print(expensive_computation(6))

#
#
# 5. Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access to a function, if a different user then responds “Access denied”.
#
# def delete_user(user, user_id):
#     print(f"User {user_id} deleted by {user['name']}")
#
# user1 = {'name': 'Alice', 'permissions': ['admin']}
# user2 = {'name': John, 'permissions': ['dev']}
# user3 = {'name': 'Kurt', 'permissions': ['test’']}
#
# Decorator to check for admin permission
def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if 'admin' in user.get('permissions', []):
            return func(user, *args, **kwargs)
        else:
            print("Access denied")
    return wrapper

@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")


user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}

delete_user(user1, 101)
delete_user(user2, 102)
delete_user(user3, 103)

#
