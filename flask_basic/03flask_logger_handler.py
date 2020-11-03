from flask import Flask
from flask.logging import default_handler

from flask_basic.logging_formatter import formatter

app = Flask(__name__)
app.config['DEBUG'] = True

"""
    flask 内置一个默认日志, 开箱即用, 一般需要根据自己的配置
"""

"""
    日志配置
    
    通过dictConfig, load解释器底层的日志配置
"""

default_handler.setFormatter(formatter)


@app.route('/', methods=['GET'])
def index_view():
    # Flask built logger use
    app.logger.info("这个视图被访问了")
    app.logger.error('a error ')
    app.logger.warning('a warning')
    return "", 200


if __name__ == '__main__':
    app.run()
