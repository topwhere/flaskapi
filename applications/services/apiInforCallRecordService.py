# -*- coding:utf-8 -*-
from sqlalchemy import true
from applications.models import ApiInforCallRecord

from applications.common.curd import auto_model_jsonify
from applications.extensions import db

# api调用记录表
class ApiInforCallRecordService():


    #Get 根据apiid查询调用记录
    @staticmethod
    def getApiInforCallRecordByApiId(api_id = ''):
        ApiInforCallRecordInfo = ApiInforCallRecord.query.filter_by(api_id=api_id).all()

        if ApiInforCallRecordInfo == []:
            return []
        data = auto_model_jsonify(ApiInforCallRecordInfo,ApiInforCallRecord)
        return data[0]
    
    #Get 根据uuid查询调用记录
    @staticmethod
    def getApiInforCallRecordByUuid(uuid = ''):
        ApiInforCallRecordInfo = ApiInforCallRecord.query.filter_by(uuid=uuid).all()

        if ApiInforCallRecordInfo == []:
            return []
        data = auto_model_jsonify(ApiInforCallRecordInfo,ApiInforCallRecord)
        return data[0]
    

    
    #Add 添加调用记录
    @staticmethod
    # uuid      用户uuid
    # api_id    api的ID
    # ip        访问ip
    def addMemberPointsAccount(uuid = '',api_id = '',ip = ''):

        addApiInforCallRecord = ApiInforCallRecord(
            uuid=uuid,
            api_id=api_id,
            ip=ip
        )
        db.session.add(addApiInforCallRecord)
        db.session.commit()
        return true