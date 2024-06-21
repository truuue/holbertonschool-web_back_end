#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
import os
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.auth import Auth
from flask_cors import (CORS, cross_origin)
from api.v1.auth.session_auth import SessionAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth_type = os.environ.get("AUTH_TYPE")
if auth_type and auth_type == "basic_auth":
    auth = BasicAuth()
elif auth_type and auth_type == "session_auth":
    auth = SessionAuth()
else:
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """ Before request """
    if auth is None:
        return

    exclude_path = ['/api/v1/status/',
                    '/api/v1/unauthorized/',
                    '/api/v1/forbidden/',
                    '/api/v1/auth_session/login/']

    if auth.require_auth(request.path, exclude_path) is not True:
        return

    if auth.authorization_header(
            request) is None and auth.session_cookie(request) is None:
        return abort(401)

    request.current_user = auth.current_user(request)
    if auth.current_user(request) is None:
        return abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5001")
    app.run(host=host, port=port, debug=True)
