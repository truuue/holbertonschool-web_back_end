#!/usr/bin/env python3
"""
Route module for the API
"""
from api.v1.auth.auth import Auth
import os


class SessionAuth(Auth):
    """ Session Authentication """
    pass


# Validate if everything inherits correctly without any overloading
session_auth = SessionAuth()
print(isinstance(session_auth, Auth))

# Validate the "switch" by using environment variables
switch = os.getenv("SESSION_AUTH_SWITCH")
if switch == "on":
    print("Session authentication is enabled")
else:
    print("Session authentication is disabled")
