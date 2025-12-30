from week_4.user import User


class Guest(User):
    def role(self):
        return "Guest"

    def access_level(self):
        return "read-only"
