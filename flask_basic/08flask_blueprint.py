from flask import Flask, Blueprint

app = Flask(__name__)

user = Blueprint('user', __name__, url_prefix='/user')


@user.route("/info/", methods=['GET'])
def info():
    print("user info")
    return "user info"


app.register_blueprint(user)


if __name__ == '__main__':
    app.run()
