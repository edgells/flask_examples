from flask_basic.blue import user


@user.route("/info/", methods=['GET'])
def info():
    return "user info"
