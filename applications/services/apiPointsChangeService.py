# -*- coding:utf-8 -*-
from sqlalchemy import true
from applications.models import ApiPointsChange

from applications.common.curd import auto_model_jsonify
from applications.extensions import db

# api积分消费记录
class ApiPointsChangeService():


    #Get 根据api_id查询积分消费记录
    @staticmethod
    def getApiPointsChangeByApiid(api_id = ''):
        ApiPointsChangeInfo = ApiPointsChange.query.filter_by(api_id=api_id).all()
        if ApiPointsChangeInfo == []:
            return []
        data = auto_model_jsonify(ApiPointsChangeInfo,ApiPointsChange)
        return data[0]
    

    #Get 根据变更记录id查询积分消费记录
    @staticmethod
    def getApiPointsChangeChangeId(change_id = ''):
        ApiPointsChangeInfo = ApiPointsChange.query.filter_by(member_points_change_id=change_id).all()
        if ApiPointsChangeInfo == []:
            return []
        data = auto_model_jsonify(ApiPointsChangeInfo,ApiPointsChange)
        return data[0]

    #Get 根据变更记录id查询积分消费记录
    @staticmethod
    def getApiPointsChangeByUuid(uuid = ''):
        ApiPointsChangeInfo = ApiPointsChange.query.filter_by(uuid=uuid).all()
        if ApiPointsChangeInfo == []:
            return []
        data = auto_model_jsonify(ApiPointsChangeInfo,ApiPointsChange)
        return data[0]
    
    #Add 添加积分消费记录
    @staticmethod
    # api_id      接口ID
    # uuid        用户uuid
    # member_points_change_id    积分消费记录关联id
    def addApiPointsChange(api_id='',uuid = '',member_points_change_id=''):
        addApiPointsChange = ApiPointsChange(
            api_id=api_id,
            uuid=uuid,
            member_points_change_id=member_points_change_id
            
        )
        db.session.add(addApiPointsChange)
        db.session.commit()
        return true