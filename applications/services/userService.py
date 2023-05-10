# -*- coding:utf-8 -*-
from math import ceil
import uuid
from sqlalchemy import false, true
from applications.models import MemberUser
from applications.common.curd import auto_model_jsonify
from applications.extensions import db
class UserService():

    #Add 根据用户账户Id添加积分变更信息
    @staticmethod
    # AccountId 账户id
    # points    积分
    # type      积分类型
    def addMemberUser(mobile = '',username = ''):
        addMemberUser = MemberUser(
            username=username,
            uuid=uuid.uuid4(),
            mobile=mobile,
            token="xxxxxx"
        )
        db.session.add(addMemberUser)
        db.session.commit()
        return true

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


    #变更用户信息
    # data = {"username":"username","username":"username"}
    @staticmethod
    def editMemberUser(uuid = '',data = {}):
        MemberUserInfo = MemberUser.query.filter_by(deleted=1).filter_by(uuid=uuid).first()

        #  不存在有效数
        if not MemberUserInfo:
            #ErrorRep -200 数据库操作异常
           return false
    
        for key, val in data.items():
            if key == "username":
                MemberUserInfo.username = val
           

        db.session.commit()
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
    
    #分页查询用户列表信息
    @staticmethod
    def getMemberUserList(page = 1,perpage = 10):
        items = MemberUser.query.order_by(MemberUser.create_at.desc()).paginate(page=page, per_page=perpage)

        total_pages = ceil(MemberUser.query.count() / perpage)
        items = auto_model_jsonify(items,MemberUser)
        result = {
            'posts': [post for post in items],
            'meta': {
                'page': page,
                'per_page': perpage,
                'total_pages': total_pages,
                'total_posts': MemberUser.query.count()
            }
        }
        return result

