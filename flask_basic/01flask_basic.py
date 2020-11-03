import uuid

from flask import Flask
from flask import request, make_response, session, redirect, url_for
from werkzeug.utils import secure_filename

from flask_basic.config import *

app = Flask(__name__)
# 引入配置
app.config.from_object(config['dev'])


# 编写第一个视图函数
@app.route("/", methods=['GET', ])
def index_view():
    # 被装饰的函数将会变成视图函数
    # 根据python函数返回值特点, 返回多个参数时, 将会被组包
    # 参数位置: 1 响应(str/byte) 2 status_code 3 headers
    return "Hello Flask", 200, {'flask_site': 'flask'}


# 编写第二个视图函数, 我们对请求来做一下处理
@app.route("/func/<string:desc>/", methods=['GET', 'POST'])
def func_view(desc):  # UrlPath

    # request 是一个代理对象, 用于在请求上下文栈中获得当前请求的request对象
    # session 同样也是一个代理对象, 原理和request 基本一致
    # make_response 用来生成这一次的响应结果

    # http 参数传递: UrlPath, QueryString, FormData, JsonData
    print(request.data)  # 处理rawData
    print(request.json)  # 处理JsonData
    print(request.args)  # 处理QueryString
    print(request.form)  # 处理FormData
    return "hello"


@app.route("/func/resp/", methods=['GET', "POST"])
def func_view_resp():
    resp = make_response(request.full_path)  # 万能的响应生成函数
    resp.set_cookie()
    return resp


@app.route("/func/upload/", methods=['POST'])
def func_view_upload():
    # 在平常的业务中, 我们经常会遇见处理用户上传文件的场景
    file = request.files['target_file']
    # 这个时候我们就可以使用Flask 封装的file对象, 进行处理
    file.save('/var/www/static/test_file.txt')  # 当然我们在真实项目中, 肯定不会这么写.
    # 这也, 暴露出来一个问题, 如果我们不处理用户上传的文件名, 后果是不堪设想的
    file.save('/var/www/static/', + secure_filename(file.filename))
    # 这里文件上传并不复杂, 哪么如果文件大, 网络情况不确定, 文件内容, 等等一系列的问题. 我们都要解决. 所以一般引入Flask-Upload, 这个扩展.

    return "Upload successful", 200


@app.route("/func/session/", methods=['GET'])
def session_view():
    sessions = uuid.uuid4()
    print(sessions)
    session['user_id'] = sessions
    resp = make_response('session生成成功')
    resp.set_cookie('python', '3.6', max_age=60)
    return resp


@app.route("/func/redirect/", methods=['GET'])
def redirect_view():
    # url_for 用来生成指定名称视图url
    # redirect 用来生成重定向响应
    # 重定向类型:    301 永久重定向
    # 临时重定向302
    return redirect(url_for('.session_view'))


if __name__ == '__main__':
    app.run()
