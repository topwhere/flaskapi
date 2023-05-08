# -*- coding:utf-8 -*-
from flask import current_app, g
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from datetime import datetime, timedelta

from applications.common.utils.jwt_util import generate_jwt
from applications.common.utils import parser





class AuthorizationView(Resource):

        def _generate_tokens(self, user_id, refresh=True):
            secret = current_app.config['JWT_SECRET']
            expiry = datetime.utcnow() + timedelta(hours=current_app.config['JWT_EXPIRY_HOURS'])

            token = generate_jwt({'user_id': user_id}, expiry, secret)

            if refresh:
                exipry = datetime.utcnow() + timedelta(days=current_app.config['JWT_REFRESH_DAYS'])
                refresh_token = generate_jwt({'user_id': user_id, 'is_refresh': True}, exipry, secret)
            else:
                refresh_token = None

            return token, refresh_token

        def post(self, mobile):
            json_parser = RequestParser()
            json_parser.add_argument('code', type=parser.regex(r'^\d{6}$'), required=True, location='json')
            args = json_parser.parse_args()
            code = args.code
            print(mobile)


            token, refresh_token = self._generate_tokens(1)

            return {'token': token, 'refresh_token': refresh_token}, 201

        def put(self):
            if g.user_id is not None and g.is_refresh is True:
                token, refresh_token = self._generate_tokens(g.user_id, refresh=False)
                return {'token': token}
            else:
                return {'message': 'Invalid refresh token'}, 403