# -*- coding: utf-8 -*-
from flask import request, g
from .jwt_util import verify_jwt



def jwt_authentication():

    g.user_id = None
    g.is_staff = None

    tokens = request.headers.get('Authorization')

    if tokens is not None and tokens.startswith('JWT '):

        token = tokens[4:]

        # 验证token
        payload = verify_jwt(token)

        if payload is not None:
            # 保存到g对象中
            g.user_id = payload.get('user_id', None)
            g.is_staff = payload.get("is_staff", None)
            g.token = token
            # g.is_refresh = payload.get('is_refresh', False)