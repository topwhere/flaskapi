# -*- coding:utf-8 -*-
from sqlalchemy import false, true
from applications.models import ApiInformation

from applications.services import ApiInforChangeRecordService


from applications.common.curd import auto_model_jsonify
from applications.extensions import db

# api信息发布管理
class ApiInformationService():


    #Get 根据id查询api信息
    @staticmethod
    def getApiInformationById(id = ''):
        ApiInformationInfo = ApiInformation.query.filter_by(id=id).all()
        if ApiInformationInfo == []:
            return []
        data = auto_model_jsonify(ApiInformationInfo,ApiInformation)
        return data[0]
    

    
    #Add 创建api
    @staticmethod
    # uuid      用户uuid
    # status    账户状态
    def addApiInformation(data={}):

        addApiInformation = ApiInformation(data)
        db.session.add(addApiInformation)
        db.session.commit()
        return true
    
    #Edit 变更api信息
    @staticmethod
    # uuid      用户uuid
    # point     积分数值
    # type      积分类型
    # is_add    操作向 ture 增加 false 减少
    def editApiInformation(uuid='',id = '',data = {}):

        ApiInformationInfo = ApiInformation.query.filter_by(id=id).first()
        
        #ErrorRep -100  不存在有效Api
        if not ApiInformationInfo:
            return false
        
        for key, val in data.items():
            if key == "id":
                #ErrorRep -101  存在非法参数
                return false
            ApiInformationInfo[key] = val
        db.session.commit()


        #存储变更记录待完善
        ApiInforChangeRecordService.addApiInforChangeRecord(id = '',uuid='',old_info = {},new_info = {})
        return true