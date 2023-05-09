# -*- coding:utf-8 -*-
from flask import Blueprint
from flask_restful import Api

from . import authorization, admin_authorization
from applications.common.utils.output import output_json


user_bp = Blueprint('user', __name__, url_prefix="/v1.0/user")
user_api = Api(user_bp, catch_all_404s=True)
user_api.representation('application/json')(output_json)

user_api.add_resource(authorization.AuthorizationView, '/auth/',
                      endpoint='Authorization')

user_api.add_resource(authorization.UserProfileView, '/profile/',
                      endpoint='UserProfile')




