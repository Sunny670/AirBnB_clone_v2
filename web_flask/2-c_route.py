#!/usr/bin/python3
"""script that starts the Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    txt = text.replace('_', ' ')
    return "C {}".format(txt)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
