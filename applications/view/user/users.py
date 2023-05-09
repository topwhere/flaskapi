# -*- coding:utf-8 -*-
from flask import current_app, g
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from datetime import datetime, timedelta

from requests import delete

from applications.common.utils.jwt_util import generate_jwt
from applications.common.utils import parser

from applications.services import UserService




class UsersView(Resource):
        # 查询
        def get(self):
            json_parser = RequestParser()
            json_parser.add_argument('mobile', type=parser.regex(r'^\d{11}$'), required=True,location='json')
            args = json_parser.parse_args()
            mobile = args.mobile

            # 调用服务层函数查询新用户
            result = UserService().getMemberUserInfoByMobile(mobile)
            return result, 200
        
        def post(self):
            json_parser = RequestParser()
            json_parser.add_argument('mobile', type=parser.regex(r'^\d{11}$'), required=True,location='json')

            args = json_parser.parse_args()
            mobile = args.mobile
            return {'mobile': mobile}, 200
        
        

        def put(self):
            if g.user_id is not None and g.is_refresh is True:
                token, refresh_token = self._generate_tokens(g.user_id, refresh=False)
                return {'token': token}
            else:
                return {'message': 'Invalid refresh token'}, 403

                    
