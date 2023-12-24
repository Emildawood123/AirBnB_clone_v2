#!/usr/bin/python3
"""Flask import moudle"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """function return what in HomePage"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """content of route /hbnb"""
    return "HBNB"


@app.route('/c/<text>')
def cis(text):
    """content of route /c/text text as a var"""
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
