from flask import Flask, jsonify
from blinker import Namespace

# 创建信号
model_signal = Namespace()

model_saved = model_signal.signal('models-signal')

app = Flask(__name__)

app.config['DEBUG'] = True


class LuckyModel:

    def __init__(self):
        self.data = {}

    def save(self, id, name):
        self.data[id] = name
        ret = model_saved.send(self, id=id, name=name)
        print(ret)


model = LuckyModel()


@model_saved.connect_via(model)
def add_balance(sender, id, name):
    print(sender, id, name)
    print("add balance 执行了")
    return True


@model_saved.connect_via(model)
def add_log(sender, id, name):
    print(sender, id, name)

    print("add log 执行了")
    return True


@app.route('/', methods=['GET', ])
def index():
    resp = jsonify({'data': "this is index page"})
    model.save(1, 'edges')
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run()
