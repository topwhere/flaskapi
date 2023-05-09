# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from flask import current_app, g
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from applications.extensions import db

from applications.common.utils.jwt_util import generate_jwt
from applications.common.utils import parser, decorators


class CreateUserView(Resource):
	"""
	創建用戶
	"""

	def post(self):
		req_parser = RequestParser()
		req_parser.add_argument('username', type=str, required=True, location='json')
		req_parser.add_argument('password', type=parser.password_format, required=True, location='json')
		req_parser.add_argument('is_staff', type=bool, required=True, location='json')

		args = req_parser.parse_args()
		username = args.username
		password = args.password
		is_staff = args.is_staff
		user = User.query.filter_by(username=username).first()

		if user:
			return {"code": 400, "command": "", "message": "用户已存在", "data": []}, 400
		# ar = Area.query.filter_by(user_name=name).first()
		# if not ar:
		#     return {"code": 400, "command": "", "message": "您尚未获得注册资格请联系管理员获取", "data": []}, 400

		else:
			if password.isdigit() or password.isalpha() or len(password) < 6:
				return {"code": 400, "command": "",
						"message": "密码格式错误,密码复杂度最低仅支持字母加数字混合且不得小于6位", "data": []}, 400
			try:
				user = User()
				user.is_staff = is_staff
				user.username = username
				# 加密层处理
				user.password = password
				db.session.add(user)
				db.session.commit()
			except Exception as e:
				current_app.logger.error(e)
				db.session.rollback()
				return {"code": 400, "command": "", "message": "用户创建错误", "data": []}, 400

			return {"code": 200, "command": "", "message": "ok", "data": {"user_id": user.id}}, 200


class AdminProfileView(Resource):
	# 管理員中間件
	method_decorators = [decorators.admin_required]

	def get(self):
		return {"code": 200, "message": "successful", "data": {}}, 200
