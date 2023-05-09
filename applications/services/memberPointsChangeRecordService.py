# -*- coding:utf-8 -*-
from sqlalchemy import false, true
from applications.models import MemberUser
from applications.common.curd import auto_model_jsonify
class MemberPointsChangeRecordService():
        #根据手机号查询用户信息
    @staticmethod
    def getMemberPointsChangeRecordByUuid(uuid = ''):
        return uuid