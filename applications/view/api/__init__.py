from flask import Flask
from applications.view.api.demo import api_demo


def register_api_views(app: Flask):
    app.register_blueprint(api_demo)