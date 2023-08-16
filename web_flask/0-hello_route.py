#!/usr/bin/python3
"""Script that starts the Flask web application"""

from flask import Flask, rendre_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
