#!/usr/bin/python3
"""
Module contains script to start flask web application
Routes :
    "/" - returns Hello HBNB!
    "/hbnb" - returns HBNB
    "/c/<text>" - returns C followed by value of text variable
    "/python/<text>" - returns Python followed by text variable or "is cool"
    if variable is empty
    "/number/n" - displays n is a number if n is an integer
    "/number_template/<n>" - displays HTML page if n is an integer
    "/number_odd_or_even/<n>" - displays HTML showing if 
    n is even or odd
"""
from flask import Flask
from flask import render_template
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Function that displays python and <text> variable
    displays "is cool" if text variable is empty
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Function that displays n is a number if n is integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Function that displays html page if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """displays a HTML page showing if n is an even or odd number"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
