#!/usr/bin/python3
"""import flask moudle"""

from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """States_lis fun"""
    dic = storage.all(State).values()
    sorted = sorted(dic, key=lambda y: y.name)
    return render_template('7-states_list.html', sorted_list=sorted)


@app.teardown_appcontext
def remove_and_reset(exc):
    """remove and reset"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
