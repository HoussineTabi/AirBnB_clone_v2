#!/usr/bin/python3
"""
The hello flask model
"""

from flask import Flask

app = Flask(__name__)


# Route definition
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
