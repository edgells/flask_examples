from flask import Flask
from flask_cache import Cache

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/", methods=['GET', 'POST'])
def index():
    return "this is index page"


if __name__ == '__main__':
    app.run()
