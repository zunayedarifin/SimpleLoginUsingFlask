from flask import Flask, render_template, redirect, url_for, request
import sqlite3
from flask import g

app = Flask(__name__)
DATABASE = 'db.sqlite3'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            email = request.form['username']
            password = request.form['password']
            cur = get_db().cursor()
            cur.execute("SELECT * FROM logininfo")
            info = cur.fetchone()
            if info[2] == email and info[3] == password:
                return render_template("profile.html")
            else:
                return "login unsuccessfull , please register"

    return render_template("login.html")


# @app.route('/register')
# def new_user():
#     return render_template("register.html")
#
#
# @app.route('/new')
# def profile():
#     return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True)
