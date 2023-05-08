# -*- coding:utf-8 -*-
from flask import jsonify


def success_api(msg: str = "成功"):
    """ 成功响应 默认值“成功” """
    return jsonify(success=True, msg=msg)


def fail_api(msg: str = "失败"):
    """ 失败响应 默认值“失败” """
    return jsonify(success=False, msg=msg)


def table_api(msg: str = "", count=0, data=None, limit=10):
    """ 动态表格渲染响应 """
    # resonpse
    res = {
        'msg': msg,
        'code': 0,
        'data': data,
        'count': count,
        'limit': limit

    }
    return jsonify(res)


def data_api(code= 200, data=None,msg: str = "ok"):
    """ 动态表格渲染响应 """
    # resonpse
    res = {
        'msg': msg,
        'code': code,
        'data': data,

    }
    return jsonify(res)
