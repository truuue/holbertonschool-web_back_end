#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request
from api.v1.views import app_views
from models.user import User
from os import getenv
from api.v1.auth import auth

app = Flask(__name__)


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """ login session module """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email == "":
        return jsonify({"error": "email missing"}), 400

    if not password or password == "":
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)

    return response
