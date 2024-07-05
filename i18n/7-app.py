#!/usr/bin/env python3
""" App module
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict
import pytz


class Config:
    """ App Config Class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale() -> str:
    """ Find the best locale to use based on query, user and request
    """
    query_locale = request.args.get("locale")
    if query_locale and query_locale in app.config["LANGUAGES"]:
        return query_locale

    if g.user:
        user_locale = g.user.get("locale")
        if user_locale and user_locale in app.config["LANGUAGES"]:
            return user_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_timezone() -> str:
    """ Find the best timezone to use based on query and user
    """
    query_timezone = request.args.get("timezone")
    try:
        return str(pytz.timezone(query_timezone))
    except pytz.exceptions.UnknownTimeZoneError:
        pass

    if g.user:
        user_timezone = g.user.get("timezone")
        try:
            return str(pytz.timezone(user_timezone))
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Dict:
    """ Get the user based to query parameter 'login_as'
    """
    login_as = request.args.get("login_as")
    if login_as is None:
        return None

    try:
        id = int(login_as)
    except Exception:
        return None

    return users.get(id)


@app.before_request
def before_request():
    """ Setup app state before every request
    """
    g.user = get_user()


@app.route("/", methods=["GET"])
def index() -> str:
    """ render index.html
    """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run()
