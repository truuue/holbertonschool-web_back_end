#!/usr/bin/env python3
""" Module of Auth views """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ A public method current_user """
        return None
