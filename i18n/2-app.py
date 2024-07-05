#!/usr/bin/env python3
""" Internationalization """
from flask import Flask, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Get locale """
    return request.accept_languages.best_match(['en', 'fr', 'es'])


@app.route('/')
def index():
    """ Home page """
    message = gettext('Hello, World!')
    return message


if __name__ == '__main__':
    app.run()
