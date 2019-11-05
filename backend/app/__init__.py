from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    
    api = Api(app, prefix='/api/v1')

    from app import routes
    routes.load(api)

    return app