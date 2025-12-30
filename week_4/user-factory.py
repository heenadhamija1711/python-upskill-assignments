from week_4.admin import Admin
from week_4.guest import Guest


class UserFactory:

    @classmethod
    def from_string(cls, data):
        # Responsible for object creation
        user_type, user_id, name = data.split(",")
        if user_type == "admin":
            return Admin(int(user_id), name)
        return Guest(int(user_id), name)

    @staticmethod
    def validate_name(name):
        # No class or instance state involved
        return name.isalpha()
