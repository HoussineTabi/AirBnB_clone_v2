#!/usr/bin/python3
"""
Script flask application displays HBNB
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text=None):
    if '_' in text:
        text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
def display_python(text=None):
    if '_' in text:
        text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)