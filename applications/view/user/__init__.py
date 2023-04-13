from flask import Flask
from applications.view.user.sms import user_sms
from applications.view.user.authorization import user_authorization
from applications.view.user.authorizationtest import user_authorizationtest


def register_user_views(app: Flask):
    app.register_blueprint(user_authorization)
    app.register_blueprint(user_authorizationtest)
    app.register_blueprint(user_sms)