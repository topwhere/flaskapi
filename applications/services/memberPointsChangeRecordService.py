# -*- coding:utf-8 -*-
from sqlalchemy import false, true
from applications.models import MemberPointsChangeRecord
from applications.common.curd import auto_model_jsonify
from applications.extensions import db
class MemberPointsChangeRecordService():
    #根据手机号查询用户信息
    @staticmethod
    def getMemberPointsChangeRecordByUuid(uuid = ''):
        return uuid
    



    #根据手机号查询用户信息
    @staticmethod
    def getMemberPointsChangeRecordInfoByMobile(mobile = ''):
        MemberPointsChangeRecordInfo = MemberPointsChangeRecord.query.filter_by(deleted=1).filter_by(mobile=mobile).all()

        if MemberPointsChangeRecordInfo == []:
            return []
        
        data = auto_model_jsonify(MemberPointsChangeRecordInfo,MemberPointsChangeRecord)
        return data[0]
    
    #根据uuid查询用户信息是否
    @staticmethod
    def chkMemberPointsChangeRecordInfoByUuid(uuid = ''):
        MemberPointsChangeRecordInfo = MemberPointsChangeRecord.query.filter_by(deleted=1).filter_by(uuid=uuid).all()

        if MemberPointsChangeRecordInfo == []:
            return []
        
        data = auto_model_jsonify(MemberPointsChangeRecordInfo,MemberPointsChangeRecord)
        return data[0]
    
    #根据手机号查询用户信息是否存在
    @staticmethod
    def chkMemberPointsChangeRecordInfoByMobile(mobile = ''):
        MemberPointsChangeRecordInfo = MemberPointsChangeRecord.query.filter_by(deleted=1).filter_by(mobile=mobile).all()

        if MemberPointsChangeRecordInfo == []:
            return 0
        else:
            return 1

    #变更用户信息
    # data = {"username":"username","username":"username"}
    @staticmethod
    def editMemberPointsChangeRecord(uuid = '',data={}):
        res =  MemberPointsChangeRecord.query.filter_by(uuid=uuid).update(data)
        MemberPointsChangeRecord.session.commit()
        if not res:
            return false
        return true
    
    #删除用户
    @staticmethod
    def delMemberPointsChangeRecord(uuid = ''):
        MemberPointsChangeRecordInfo = MemberPointsChangeRecord.query.filter_by(deleted=1).filter_by(uuid=uuid).first()

        #  不存在有效数据删除失败
        if not MemberPointsChangeRecordInfo:
           return false
        
        MemberPointsChangeRecordInfo.deleted = 2
        db.session.commit()

        return true