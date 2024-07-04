#!/usr/bin/env python3
""" Internationalization and Localization (i18n) with Flask """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Home page """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
