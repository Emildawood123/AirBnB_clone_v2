#!/usr/bin/python3
"""import flask moudle"""

from flask import Flask, render_template
from models import storage
from models.state import State



app = Flask()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """states_list fun"""
    dic = storage.all(State).values()
    sorted = sorted(dic, key=lambda y: y.name)
    return render_template('7-states_list.html', sorted_list=sorted)


@app.teardown_appcontext
def terminate():
    """teminate to reload by close"""
    storage.close()


if __name__ == "__main__":
    """for pass task"""
    app.run(host='0.0.0.0', port=5000)
