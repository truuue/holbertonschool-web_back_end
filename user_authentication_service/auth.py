#!/usr/bin/env python3
""" Hash password module """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ Module that hash password """
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password


class Auth:
    """ Auth class to interact with the authentication database. """

    def __init__(self):
        """ Constructor method """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register a user and return the User object """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
