# -*- coding:utf-8 -*-
from sqlalchemy import true
from applications.models import MemberPointsChangeRecord
from applications.common.curd import auto_model_jsonify
from applications.extensions import db

# 用户账户积分变更记录
class MemberPointsChangeRecordService():


    #Get 根据uuid查询用户积分列表
    @staticmethod
    def getMemberPointsChangeRecordInfoByUuid(uuid = ''):
        MemberPointsChangeRecordInfo = MemberPointsChangeRecord.query.filter_by(uuid=uuid).all()

        if MemberPointsChangeRecordInfo == []:
            return []
        
        data = auto_model_jsonify(MemberPointsChangeRecordInfo,MemberPointsChangeRecord)
        return data[0]
    
    #Get 根据用户账户Id查询用户积分列表
    @staticmethod
    def getMemberPointsChangeRecordInfoByUAccountId(AccountId = ''):
        MemberPointsChangeRecordInfo = MemberPointsChangeRecord.query.filter_by(account_id=AccountId).all()

        if MemberPointsChangeRecordInfo == []:
            return []
        
        data = auto_model_jsonify(MemberPointsChangeRecordInfo,MemberPointsChangeRecord)
        return data[0]
    
    #Add 根据用户账户Id添加积分变更信息
    @staticmethod
    # AccountId 账户id
    # points    积分
    # type      积分类型
    def addMemberPointsChangeRecordByAccountId(AccountId = '',points = '',type = 1):

        addMemberPointsChangeRecord = MemberPointsChangeRecord(
            account_id=AccountId,
            points=points,
            type=type
        )
        db.session.add(addMemberPointsChangeRecord)
        db.session.commit()
        return true
    
    #Add 根据用户Uuid添加积分变更信息
    @staticmethod
    # uuid 用户uuid
    # points    积分
    # type      积分类型
    def addMemberPointsChangeRecordByUuid(uuid = '',points = '',type = 1):

        addMemberPointsChangeRecord = MemberPointsChangeRecord(
            uuid=uuid,
            points=points,
            type=type
        )
        db.session.add(addMemberPointsChangeRecord)
        db.session.commit()
        return true