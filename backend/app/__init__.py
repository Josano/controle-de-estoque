from flask import Flask
from flask_restful import Api

def create_app(config_name):
    app = Flask(__name__)
    api = Api(app, prefix='/api/v1')

    return app