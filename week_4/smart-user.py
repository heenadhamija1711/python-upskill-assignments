from week_4.user import User


class SmartUser(User):

    def __str__(self):
        return f"{self.name} ({self.role()})"

    def __repr__(self):
        return f"SmartUser(id={self.user_id}, name='{self.name}')"

    def __len__(self):
        # business metric: length of username
        return len(self.name)

    def __eq__(self, other):
        return self.user_id == other.user_id

    def __lt__(self, other):
        return self.user_id < other.user_id

    def __call__(self):
        return f"User {self.name} executed as function"
