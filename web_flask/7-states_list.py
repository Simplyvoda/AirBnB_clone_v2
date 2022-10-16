#!/usr/bin/python3
"""Module contains script that starts flask web app
    - uses storage to fetch data from storage engine
    - contains method to remove current SQLAlchemy session
"""
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """displays HTML page"""
    states = storage.all("State")
    return render_template('7-states_list.html')


@app.teardown_appcontext
def teardown_db():
    """Removes current alchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
