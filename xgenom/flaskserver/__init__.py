"""
The recipes Blueprint handles the creation, modification, deletion,
and viewing of recipes for this application.
"""
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

api = Api()

def create_app(config_filename=None, **kwargs):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)

    return app


def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    api.init_app(app)


def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from xgenom.flaskserver.recipes import recipes_blueprint
    from xgenom.flaskserver.auth.blueprint_auth import authentication

    app.register_blueprint(recipes_blueprint)
    app.register_blueprint(authentication, url_prefix="/api/auth")
