# -*- coding:utf-8 -*-
from sqlalchemy import false, true
from applications.models import ApiInforChangeRecord

from applications.common.curd import auto_model_jsonify
from applications.extensions import db

# api变更记录表
class ApiInforChangeRecordService():


    #Get 根据api_id查询变更记录信息
    @staticmethod
    def getApiInforChangeRecordByApiId(api_id = ''):
        ApiInforChangeRecordInfo = ApiInforChangeRecord.query.filter_by(api_id=api_id).all()
        if ApiInforChangeRecordInfo == []:
            return []
        
        data = auto_model_jsonify(ApiInforChangeRecordInfo,ApiInforChangeRecord)
        return data[0]
    
    #Get 根据账户uuid查询变更记录信息
    @staticmethod
    def getMemberPointsAccountById(uuid = ''):
        ApiInforChangeRecordInfo = ApiInforChangeRecord.query.filter_by(edit_uuid=uuid).all()
        if ApiInforChangeRecordInfo == []:
            return []
        data = auto_model_jsonify(ApiInforChangeRecordInfo,ApiInforChangeRecord)
        return data[0]
    

    
    #Add 添加变更记录信息
    @staticmethod
    # api_id         api的id
    # edit_uuid      用户的uuid
    # old_info      变更前数据
    # new_info      变更后数据
    # edit_mark      变更表述    
    def addApiInforChangeRecord(api_id = '',edit_uuid='',old_info = {},new_info = {},edit_mark=''):
        addApiInforChangeRecord = ApiInforChangeRecord(
            api_id=api_id,
            edit_uuid=edit_uuid,
            old_info=old_info,
            new_info=new_info,
            edit_mark=edit_mark 
        )
        db.session.add(addApiInforChangeRecord)
        db.session.commit()
        return true