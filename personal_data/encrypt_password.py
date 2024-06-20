#!/usr/bin/env python3
""" Encrypting passwords module """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Hash a password """
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check if a password is valid """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
