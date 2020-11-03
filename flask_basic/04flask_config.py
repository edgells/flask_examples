from flask import Flask


class Config:
    """
        注意Flask 的配置应该是大写格式
        * 除了Flask本身的配置写在配置类里面, 有些Flask扩展也需要将配置写在这里
    """
    ENV = 'development'     # 确定当前应用环境
    DEBUG = True            # 确定应用模式
    SECRET_KEY = ''         # 应用安全key


app = Flask(__name__)
app.config.from_object(Config)


if __name__ == '__main__':
    app.run()