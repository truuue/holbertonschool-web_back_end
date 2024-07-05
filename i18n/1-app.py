#!/usr/bin/env python3
""" Internationalization """
from flask import Flask, render_template
from flask_babel import Babel, get_locale, get_timezone

app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


class Config:
    """ Config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """ Home page """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
