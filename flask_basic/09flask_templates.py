from concurrent.futures.thread import ThreadPoolExecutor

from flask import Flask, render_template, flash, redirect, url_for
from flask import current_app, request

app = Flask(__name__)


app.config['THREAD_WORKER_NUM'] = 10
app.config['SECRET_KEY'] = 'asdfasdfasdfsadfa'
app.tpool = ThreadPoolExecutor(app.config['THREAD_WORKER_NUM'])


def _send_mail(message):
    try:
        pass
    except Exception as e:
        current_app.logger.info(e)


@app.route("/", methods=['GET'])
def index():
    flash("hello world")
    return render_template("index.html")


@app.route("/login/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = "Invalid credentials"

        else:
            flash("You were successfully logged in")
            return redirect(url_for('index'))

    return render_template("login.html", error=error)


if __name__ == '__main__':
    app.run()
