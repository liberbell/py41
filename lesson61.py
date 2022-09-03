from crypt import methods
import sqlite3
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response


app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello world!</p>"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("test_sqlite.db")
    return db

def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@app.route('/top')
def hello_world():
    return "Top!"

@app.route("/hello")
@app.route("/hello/<username>")
def hello_world2(username=None):
    # return "<p>Hello world! {}</p>".format(username)
    return render_template("hello.html", username=username)

@app.route("/post", methods=["POST", "PUT", "DELETE"])
def show_post():
    return str(request.values["username"])


def main():
    app.debug = True
    app.run()

if __name__ == "__main__":
    main()