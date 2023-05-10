# -*- coding:utf-8 -*-
from flask import Blueprint
from flask_restful import Api

from . import authorization, authorizationtest,users
from applications.common.utils.output import output_json



user_bp = Blueprint('user', __name__, url_prefix="/v1.0/user/")
user_api = Api(user_bp, catch_all_404s=True)
user_api.representation('application/json')(output_json)

# url路径 xxx:8080/v1.0/user/sms/codes
user_api.add_resource(authorization.AuthorizationView, '/sms/codes/',
                      endpoint='Authorization')

#用户创建相关逻辑
user_api.add_resource(users.UsersView, '/info/',endpoint='Users')
#查询用户列表
user_api.add_resource(users.UsersListView, '/getuserlist/',endpoint='UsersList')


user_api.add_resource(authorizationtest.AuthorizationTestView, '/authorizations/',
                      endpoint='AuthorizationTest')
