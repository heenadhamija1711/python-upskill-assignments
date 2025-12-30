class User:
    active_users = 0  # class-level attribute

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        User.active_users += 1

    def role(self):
        return "Generic User"

    def access_level(self):
        return "basic"

    def deactivate(self):
        User.active_users -= 1

    def __del__(self):
        User.active_users -= 1