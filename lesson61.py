from unicodedata import name
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "hello world"

@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

def main():
    app.debug = True
    app.run()

if __name__ == "__main__":
    main()