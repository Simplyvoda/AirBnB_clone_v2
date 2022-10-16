#!/usr/bin/python3
"""
Module contains script to start flask web application
Routes :
"/" - returns Hello HBNB!
"/hbnb" - returns HBNB
"/c/<text>" - returns C followed by value of text variable
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Function that returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function that returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Function that displays C and text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
