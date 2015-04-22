# -*- coding: utf-8 -*-

# Flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Twisted!"

# Twisted
from flask.ext.twisted import Twisted
twisted = Twisted(app)

# Main
if __name__ == "__main__":
    app.run()
