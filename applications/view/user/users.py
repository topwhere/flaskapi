# -*- coding:utf-8 -*-
from flask import current_app, g
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from datetime import datetime, timedelta

from requests import delete
from sqlalchemy import true

from applications.common.utils.jwt_util import generate_jwt
from applications.common.utils import parser

from applications.services import UserService




class UsersView(Resource):
        json_parser = RequestParser()
        # 查询用户信息
        def get(self):
            self.json_parser.add_argument('mobile', type=parser.regex(r'^\d{11}$'), required=True,location='json')
            args = self.json_parser.parse_args()
            mobile = args.mobile

            # 调用服务层函数查询新用户
            result = UserService().getMemberUserInfoByMobile(mobile)
            return result, 200
        
        # 创建用户
        def post(self):
            self.json_parser.add_argument('mobile', type=parser.regex(r'^\d{11}$'), required=True,location='json')
            args = self.json_parser.parse_args()
            mobile = args.mobile

            # 调用服务层函数-查询用户是否存在
            result = UserService().getMemberUserInfoByMobile(mobile)
            if result != [] :
                return {'msg': "用户已存在请勿重复创建"}, 400
            
            # 调用服务层函数-创建用户
            result = UserService().addMemberUser(mobile)
            if result != true:
                 return {'msg': "用户创建失败"}, 400
            
            return {'msg': "创建成功"}, 200
        
        # 编辑用户
        def put(self):
            if g.uuid is not None and g.is_refresh is True:
                token, refresh_token = self._generate_tokens(g.user_id, refresh=False)
                return {'token': token}
            else:
                return {'message': 'Invalid refresh token'}, 400

                    
class UsersListView(Resource):
        json_parser = RequestParser()
            # 查询
        def get(self):
            # args = self.json_parser.parse_args()
            pages = 1
            count = 10
            # 调用服务层函数查询新用户
            result = UserService().getMemberUserList(pages,count)
            return result, 200