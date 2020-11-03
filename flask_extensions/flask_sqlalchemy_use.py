from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import pool

import eventlet

# 实例Flask app
app = Flask(__name__)

# load 配置
app.config['DEBUG'] = True
app.config['SERVER_NAME'] = "127.0.0.1:5000"

# load sqlalchemy 配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://tmp/test.db'
app.config['SQLALCHEMY_BINDS'] = {}  # 注意如果我们在配置中配置了 uri 这个地方就要注意
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}  # 传递给sqlalchemy engine 的参数
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


@app.route("/", methods=['GET'])
def index():
    print(url_for('.index'))
    return "flask world"


if __name__ == '__main__':
    eventlet.monkey_patch()
    app.run()
