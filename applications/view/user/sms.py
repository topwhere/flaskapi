# -*- coding:utf-8 -*-
import random
from flask import request, current_app
from flask_restful import Resource
from applications.common.utils.limiter import limiter as lmt
from flask_limiter.util import get_remote_address

from . import constants


class SMSVerificationCodeResource(Resource):
	# 短信验证码
	# 增加限流
	error_msg = 'Too many requests.'

	decorators = [
		lmt.limit(constants.LIMIT_SMS_VERIFICATION_CODE_BY_MOBILE,
				key_func=lambda: request.view_args['mobile'],
				error_msg=error_msg),
		lmt.limit(constants.LIMIT_SMS_VERIFICATION_CODE_BY_IP,
				key_func=get_remote_address,
				error_msg=error_msg)
	]

	def get(self, mobile):
		code = '{:0>6d}'.format(random.randint(0, 999999))
		current_app.redis_master.setex('app:code:{}'.format(mobile), constants.SMS_VERIFICATION_CODE_EXPIRES, code)
		# send_verification_code.delay(mobile, code)
		return {'mobile': mobile}
