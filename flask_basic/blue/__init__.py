from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')

from flask_basic.blue.views import *