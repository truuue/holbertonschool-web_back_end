#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar

""" Module of Auth views """


class Auth:
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if excluded_paths and path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        if request is None or 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        if request is None:
            return None
        else:
            return request
