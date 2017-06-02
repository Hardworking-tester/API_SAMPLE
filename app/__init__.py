# encoding:utf-8
# author:wwg
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
bootstrap = Bootstrap()
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)
    db.init_app(app)
    from .atuo import auto as auth_blueprint
    app.register_blueprint(auth_blueprint)
    app.config['SECRET_KEY'] = 'wwg'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123abc@localhost/api_test2"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    return app
