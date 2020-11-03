from flask import Flask

from flask_basic.config import *

app = Flask(__name__)

# load 配置
app.config['DEBUG'] = True
app.config['SERVER_NAME'] = "127.0.0.1:5000"


if __name__ == '__main__':
    app.run()
