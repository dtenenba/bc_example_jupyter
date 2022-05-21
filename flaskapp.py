#!/usr/bin/python3

import sys

from flask import Flask
app = Flask(__name__)

host = sys.argv[1]
port = int(sys.argv[2])


@app.route(f"/node/{host}/{port}/login")
def hello():
    return 'hello'


if __name__ == "__main__":
    app.run(port=port, host="0.0.0.0") 
