import sys
import importlib

importlib.reload(sys)
from flask import *
import flask_restful

app = Flask(__name__)
api = flask_restful.Api(app)


class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello': 1, 'donghu': 2}  # 接口返回值


api.add_resource(HelloWorld, '/login', methods=['GET'])  # 页面路径

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=11111)  # 请求地址，以及端口