class UserRepository:

    def __init__(self, users):
        self.users = users

    def stream_users(self):
        for user in self.users:
            yield user  # lazy streaming
