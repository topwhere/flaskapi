# -*- coding:utf-8 -*-
from sqlalchemy import false, true
from applications.models import MemberPointsAccount
from applications.services import MemberPointsChangeRecordService

from applications.common.curd import auto_model_jsonify
from applications.extensions import db

# 用户积分账户
class memberPointsAccountService():


    #Get 根据uuid查询用户积分账户信息
    @staticmethod
    def getMemberPointsAccountByUuid(uuid = ''):
        MemberPointsChangeRecordInfo = MemberPointsAccount.query.filter_by(uuid=uuid).all()

        if MemberPointsChangeRecordInfo == []:
            return []
        
        data = auto_model_jsonify(MemberPointsChangeRecordInfo,MemberPointsAccount)
        return data[0]
    
    #Get 根据账户id查询用户积分账户信息
    @staticmethod
    def getMemberPointsAccountById(id = ''):
        MemberPointsChangeRecordInfo = MemberPointsAccount.query.filter_by(id=id).all()

        if MemberPointsChangeRecordInfo == []:
            return []
        
        data = auto_model_jsonify(MemberPointsChangeRecordInfo,MemberPointsAccount)
        return data[0]
    

    
    #Add 创建用户账户
    @staticmethod
    # uuid      用户uuid
    # status    账户状态
    def addMemberPointsAccount(uuid = ''):

        addMemberPointsChangeRecord = MemberPointsAccount(
            uuid=uuid,
            status=1
        )
        db.session.add(addMemberPointsChangeRecord)
        db.session.commit()
        return true
    
    #Edit 账户积分变更
    @staticmethod
    # uuid      用户uuid
    # point     积分数值
    # type      积分类型
    # is_add    操作向 ture 增加 false 减少
    def editMemberPointsAccount(uuid = '',point = 0,type = 1,is_add = true):

        MemberPointsAccountInfo = MemberPointsAccount.query.filter_by(uuid=uuid).first()
        
        #ErrorRep 202  不存在有效账户
        if not MemberPointsAccountInfo:
            return false
        
        #ErrorRep 203   积分余额不足
        if MemberPointsAccountInfo.current_points < point:
            return false
        

        #ErrorRep -204  积分账户表操作
        if is_add == true:
            MemberPointsAccountInfo.historical_points +=point
            MemberPointsAccountInfo.current_points += point 
        if is_add == false:
            MemberPointsAccountInfo.current_points -= point
        db.session.commit()

        # 积分记录表操作
        MemberPointsChangeRecordService.addMemberPointsChangeRecordByAccountId(MemberPointsAccountInfo.id,point,type)
        return true
    

    #Edit 账户信息变更,根据uuid
    @staticmethod
    def EditMemberPointsAccount(uuid = '',data={}):
        MemberPointsAccountInfo = MemberPointsAccount.query.filter_by(uuid=uuid).first()
        #ErrorRep -202  不存在有效账户
        if not MemberPointsAccountInfo:
            return false
        
        res = MemberPointsAccountInfo = MemberPointsAccount.query.filter_by(uuid=uuid).update(data)
        MemberPointsAccountInfo.session.commit()
        if not res:
            #ErrorRep -200 数据库操作异常
            return false
        return true
    