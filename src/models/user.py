from src.common.database import Database


class User:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one('users', {'email': email})
        if data is not None:
            return cls(**data)

    def get_by_id(self):
        pass

    def login_valid(self):
        # check loging and email information
        pass

    def register(self):
        pass

    def login(self):
        pass

    def get_blogs(self):
        pass