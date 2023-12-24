#!/usr/bin/python3
"""Flask import moudle"""
from flask import Flask, abort, render_template

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


@app.route('/python/')
def python():
    """to show content for /python/"""
    return "Python is cool"


@app.route('/python/<text>')
def pythonis(text):
    """to show content for /python/text as variable"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<n>')
def number(n):
    """if number show it else it take him 404"""
    try:
        n = int(n)
        return f"{n} is a number"
    except Exception:
        abort(404)


@app.route('/number_template/<n>')
def number_tamplete(n):
    try:
        n = int(n)
        return render_template('5-number.html', number=n)
    except Exception:
        abort(404)


@app.route('/number_odd_or_even/<n>')
def number_even_odd(n):
    try:
        n = int(n)
        return render_template('6-number_odd_or_even.html', number=n)
    except Exception:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
