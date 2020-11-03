
__all__ = ['config', ]
"""

    flask 配置的使用方式有多种, 我们暂时只需要知道的一种, python object 形式
    
    常见配置其实我们也可以在源码的一部分地方找出来
"""

class Config:
    DEBUG = None
    SECRET_KEY = '' or r"8o\xbe%\x00A\xff<TQ1\xa0\x0f\x83oL\xf9\x82D-\xef\x84\xf0V\xcfc\x00f\x82\x0b'\xe82\xbbYFmE\x93R\x15\x7fU&\x8c\x89\xadBU\xa0\x7f\x90\xe36t\xeb\xae\x8az\xfd\xd8W\r\x02"

class DevConfig(Config):
    DEBUG = True
    ENV = 'development'

config = {
    'dev': DevConfig
}