import os

from flask import Flask, request
from werkzeug.utils import secure_filename

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制文件上传大小为16m

upload_folder = os.path.join(BASE_DIR, 'files')
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)

app.config['UPLOAD_FOLDER'] = upload_folder

ALLOWED_FILE_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'word', 'xls'}


def allowed_file(filename: str):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXTENSIONS


@app.route('/uploads/', methods=['POST'])
def file_upload():
    print(request.files)

    # 保存文件
    file = request.files['files']
    # 检查扩展名是否合法
    if file is None:
        return {'data': '上传文件有误'}, 400

    if file.filename is '' and not allowed_file(file.filename):
        return {'data': '文件名错误'}, 400

    # 文件重复上传, 造成的版本问题
    # 文件上传是一件耗时任务, 所以我们应该将文件上传服务, 单独抽离出来, 尽量不要影响主业务运行
    filename = secure_filename(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))  # 处理成安全的文件名
    file.save(filename)  # 注意这里的文件应该要做一下处理

    return "uploads file successful", 200


if __name__ == '__main__':
    app.run()
