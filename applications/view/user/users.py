# -*- coding:utf-8 -*-
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

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
            """
            判断字符串是否为合法的 UUID 格式。
            """
            self.json_parser.add_argument('uuid', type=parser.regex(r'^[a-f0-9]{8}-[a-f0-9]{4}-[4|5][a-f0-9]{3}-[8|9|aA|bB][a-f0-9]{3}-[a-f0-9]{12}$'), required=True,location='json')
            self.json_parser.add_argument('data',type=dict, required=True,location='json')
            args = self.json_parser.parse_args()
            
            uuid = args.uuid
            data = args.data

            # 调用服务层函数-查询用户是否存在
            result = UserService().chkMemberUserInfoByUuid(uuid)
            if result == [] :
                return {'msg': "不存在有效用户"}, 400
            
            # 调用服务层函数-变更用户信息
            result = UserService().editMemberUser(uuid,data)
            if result != true:
                 return {'msg': "用户信息变更失败"}, 400
            
            return {'msg': "更新成功"}, 200
        
        
        #删除用户
        def delete(self):
            """
            判断字符串是否为合法的 UUID 格式。
            """
            self.json_parser.add_argument('uuid', type=parser.regex(r'^[a-f0-9]{8}-[a-f0-9]{4}-[4|5][a-f0-9]{3}-[8|9|aA|bB][a-f0-9]{3}-[a-f0-9]{12}$'), required=True,location='json')
            args = self.json_parser.parse_args()
            uuid = args.uuid

            # 调用服务层函数-查询用户是否存在
            result = UserService().chkMemberUserInfoByUuid(uuid)
            if result == [] :
                return {'msg': "不存在有效用户"}, 400
            
            # 调用服务层函数-变更用户信息
            result = UserService().delMemberUser(uuid)
            if result != true:
                 return {'msg': "用户删除失败"}, 400
            
            return {'msg': "删除成功"}, 200

                    
class UsersListView(Resource):
        json_parser = RequestParser()
            # 查询
        def get(self):
            # args = self.json_parser.parse_args()
            self.json_parser.add_argument('pages', type=int, required=True,location='json')
            self.json_parser.add_argument('count',type=int, required=True,location='json')
            args = self.json_parser.parse_args()
            pages = args.pages
            count = args.count
            # 调用服务层函数查询新用户
            result = UserService().getMemberUserList(pages,count)
            return result, 200