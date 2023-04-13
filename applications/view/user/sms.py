import random
from flask import Blueprint,request, current_app
from flask_restful import Api,Resource
from applications.common.utils.limiter import limiter as lmt
from applications.common.utils.output import output_json
from flask_limiter.util import get_remote_address

from . import constants

user_sms = Blueprint('user_sms', __name__, url_prefix='/user/sms')


user_api = Api(user_sms, catch_all_404s=True)
user_api.representation('application/json')(output_json)


class SMSVerificationCodeResource(Resource):
    # 短信验证码
    # 增加限流
    error_message = 'Too many requests.'

    decorators = [
        lmt.limit(constants.LIMIT_SMS_VERIFICATION_CODE_BY_MOBILE,
                  key_func=lambda: request.view_args['mobile'],
                  error_message=error_message),
        lmt.limit(constants.LIMIT_SMS_VERIFICATION_CODE_BY_IP,
                  key_func=get_remote_address,
                  error_message=error_message)
    ]

    def get(self, mobile):
        code = '{:0>6d}'.format(random.randint(0, 999999))
        current_app.redis_master.setex('app:code:{}'.format(mobile), constants.SMS_VERIFICATION_CODE_EXPIRES, code)
        # send_verification_code.delay(mobile, code)
        return {'mobile': mobile}


user_api.add_resource(SMSVerificationCodeResource, '/sms/codes/<int:mobile>', endpoint='SMSVerificationCode')