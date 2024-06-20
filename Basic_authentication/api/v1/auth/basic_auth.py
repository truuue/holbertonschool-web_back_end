#!/usr/bin/env python3
""" Module of Basic Auth views """
from api.v1.auth.auth import Auth
import base64
import binascii
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Class to manage the API authentication """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Method that extracts the base64 value from the Authorization header
        """
        if authorization_header is None or not isinstance(
            authorization_header, str) or not authorization_header.startswith(
                'Basic '):
            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Method that decodes a Base64 string
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Method that extracts the user email and
        password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Method that returns the User instance
        based on his email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            found_users = User.search({'email': user_email})
        except Exception:
            return None

        for user in found_users:
            if user.is_valid_password(user_pwd):
                return user

        return None


def current_user(self, request=None) -> TypeVar('User'):
    """
    Method that retrieves the User instance for a request
    """
    if request is None:
        return None

    authorization_header = self.authorization_header(request)
    base64_authorization_header = self.extract_base64_authorization_header(
        authorization_header)
    decoded_base64_authorization_header = self.decode_base64_authorization_header(
        base64_authorization_header)
    user_email, user_pwd = self.extract_user_credentials(
        decoded_base64_authorization_header)
    user = self.user_object_from_credentials(user_email, user_pwd)

    return user
