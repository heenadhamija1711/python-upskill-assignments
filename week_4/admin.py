from week_4.user import User


class Admin(User):
    def role(self):
        return "admin.py"

    def access_level(self):
        return "all"

