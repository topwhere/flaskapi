# -*- coding:utf-8 -*-
from sqlalchemy import true
from applications.models import Log

from applications.extensions import db

# 日志服务表
class logService():

    #Add 添加日志记录
    @staticmethod
    def addLog(data = {}):
        addLog = Log(data)
        db.session.add(addLog)
        db.session.commit()
        return true
   