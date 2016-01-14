import uuid

from flask import session

from src.common.database import Database


class User:

    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one('users', {'email': email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one('users', {'_id': _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        # check if user exists
        if user is not None:
            return user.password == password
        else:
            # User does not exist
            return False

    @staticmethod
    def register(email, password):
        # check is email exists and if so return None
        user = User.get_by_email(email)
        if user is None:
            # allow to register
            new_user = User(email, password)
            new_user.save_to_mongo()
            session['email'] = email
        else:
            # user exists
            return False

    @staticmethod
    def login(user_email):
        # we have already checked that login is valid
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def json(self):
        return {
            'email': self.email,
            'password': self.password,
            '_id': self._id
        }

    def get_blogs(self):
        pass