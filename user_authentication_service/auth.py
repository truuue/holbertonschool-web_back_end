#!/usr/bin/env python3
""" Hash password module """
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ Module that hash password """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password


def _generate_uuid() -> str:
    """ Generate a new UUID """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ Check if the login credentials are valid """
        try:
            user = self._db.find_user_by(email=email)
            hashed_password = user.hashed_password
            return bcrypt.checkpw(password.encode(), hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ create_session: returns the session ID as a string """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Get a user by session ID. """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except Exception:
            return None

        return user
