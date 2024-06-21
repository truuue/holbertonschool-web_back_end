#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request
from api.v1.views import app_views
from models.user import User
import os

app = Flask(__name__)


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """ auth sessions login route"""
    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    all_users = User.search({"email": email})
    if not all_users:
        return jsonify({"error": "no user found for this email"}), 404

    current_user = all_users[0]
    if not current_user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session = auth.create_session(current_user.id)
    SESSION_NAME = os.getenv('SESSION_NAME')

    setCookie = jsonify(current_user.to_json())
    setCookie.set_cookie(SESSION_NAME, session)

    return setCookie
