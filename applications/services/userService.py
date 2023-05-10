# -*- coding:utf-8 -*-
from sqlalchemy import false, true
from applications.models import MemberUser
from applications.common.curd import auto_model_jsonify
from applications.extensions import db
class UserService():


    #根据手机号查询用户信息
    @staticmethod
    def getMemberUserInfoByMobile(mobile = ''):
        MemberUserInfo = MemberUser.query.filter_by(deleted=1).filter_by(mobile=mobile).all()

        if MemberUserInfo == []:
            return []
        
        data = auto_model_jsonify(MemberUserInfo,MemberUser)
        return data[0]
    
    #根据uuid查询用户信息
    @staticmethod
    def chkMemberUserInfoByUuid(uuid = ''):
        MemberUserInfo = MemberUser.query.filter_by(deleted=1).filter_by(uuid=uuid).all()

        if MemberUserInfo == []:
            return []
        
        data = auto_model_jsonify(MemberUserInfo,MemberUser)
        return data[0]
    
    #根据手机号查询用户信息是否存在
    @staticmethod
    def chkMemberUserInfoByMobile(mobile = ''):
        MemberUserInfo = MemberUser.query.filter_by(deleted=1).filter_by(mobile=mobile).all()

        if MemberUserInfo == []:
            return 0
        else:
            return 1

    #变更用户信息
    # data = {"username":"username","username":"username"}
    @staticmethod
    def editMemberUser(uuid = '',data={}):
        res =  MemberUser.query.filter_by(uuid=uuid).update(data)
        MemberUser.session.commit()
        if not res:
            #ErrorRep -200 数据库操作异常
            return false
        return true
    
    #删除用户
    @staticmethod
    def delMemberUser(uuid = ''):
        MemberUserInfo = MemberUser.query.filter_by(deleted=1).filter_by(uuid=uuid).first()

        #  不存在有效数据删除失败
        if not MemberUserInfo:
            #ErrorRep -200 数据库操作异常
           return false
        
        MemberUserInfo.deleted = 2
        db.session.commit()

        return true
