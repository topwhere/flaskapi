from flask import Flask
from applications.view.api.ceshi import api_ceshi
from applications.view.api.users import api_users


def register_api_views(app: Flask):
    app.register_blueprint(api_users)
    app.register_blueprint(api_ceshi)