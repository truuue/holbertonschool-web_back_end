#!/usr/bin/env python3
""" Hash password module """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Module that hash password """
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password
