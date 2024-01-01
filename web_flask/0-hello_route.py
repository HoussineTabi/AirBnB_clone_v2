#!/usr/bin/python3
"""
The hello flask model
"""


import flask
app = flask.Flask(__name__)
@app.route('/')
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(debug=True)
