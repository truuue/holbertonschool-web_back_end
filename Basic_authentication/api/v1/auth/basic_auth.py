#!/usr/bin/env python3
""" Module of Basic Auth views """
from api.v1.auth.auth import Auth
import base64


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
