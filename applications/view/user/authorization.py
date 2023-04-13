from flask import Blueprint, current_app, g
from flask_restful import Api,Resource
from flask_restful.reqparse import RequestParser
from datetime import datetime, timedelta

from applications.common.utils.output import output_json
from applications.common.utils.jwt_util import generate_jwt
from applications.common.utils import parser


user_authorization = Blueprint('user_authorization', __name__, url_prefix='/user/authorization')


user_api = Api(user_authorization, catch_all_404s=True)
user_api.representation('application/json')(output_json)


class AuthorizationResource(Resource):
        #��֤

        def _generate_tokens(self, user_id, refresh=True):
            #����token ��refresh_token
            #:param user_id: �û�id
            #:return: token, refresh_token
            # �䷢JWT
            secret = current_app.config['JWT_SECRET']
            # ���ɵ���token�� refresh_token
            expiry = datetime.utcnow() + timedelta(hours=current_app.config['JWT_EXPIRY_HOURS'])

            token = generate_jwt({'user_id': user_id}, expiry, secret)

            if refresh:
                exipry = datetime.utcnow() + timedelta(days=current_app.config['JWT_REFRESH_DAYS'])
                refresh_token = generate_jwt({'user_id': user_id, 'is_refresh': True}, exipry, secret)
            else:
                refresh_token = None

            return token, refresh_token

        def post(self):
            #��¼����token
            json_parser = RequestParser()
            json_parser.add_argument('mobile', type=parser.mobile, required=True, location='json')
            json_parser.add_argument('code', type=parser.regex(r'^\d{6}$'), required=True, location='json')
            args = json_parser.parse_args()
            mobile = args.mobile
            code = args.code

            # ��redis�л�ȡ��֤��
            key = 'app:code:{}'.format(mobile)
            # �����û���jwt token
            # ��payload �����û���ʲô��Ϣ
            # user_id  һ��
            #
            # ����Ҫ��tokenȡ������ ����Ҫ��ѯ���ݿ�ʱ��
            # mobile ��һ��
            # user_name  ��һ��

            token, refresh_token = self._generate_tokens(1)

            return {'token': token, 'refresh_token': refresh_token}, 201

        def put(self):
            #ˢ��token
            #:return:
            if g.user_id is not None and g.is_refresh is True:
                token, refresh_token = self._generate_tokens(g.user_id, refresh=False)
                return {'token': token}
            else:
                return {'message': 'Invalid refresh token'}, 403


user_api.add_resource(AuthorizationResource, '/authorization', endpoint='Authorization')