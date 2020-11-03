from datetime import datetime, date

from flask import Flask
from flask.views import MethodView

from flask_basic.config import config


app = Flask(__name__)

app.config.from_object(config['dev'])
app.config['JSON_AS_ASCII'] = False

class DemoView(MethodView):


    def get(self):
        return {"data":{
            'datetime': datetime.now(),
            'name': '老王'
        }}


app.add_url_rule("/", view_func=DemoView.as_view('demo'))

if __name__ == '__main__':
    app.run()