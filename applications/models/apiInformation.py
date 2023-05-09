# -*- coding:utf-8 -*-
import datetime
from applications.extensions import db


class ApiInformation(db.Model):
    __tablename__ = 'api_information'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='自增id')
    host = db.Column(db.String(255, collation='utf8mb4_general_ci'), nullable=False, default='', comment='接口地址')
    name = db.Column(db.String(255, collation='utf8mb4_general_ci'), nullable=False, default='', comment='接口名称')
    api_mark = db.Column(db.Text(collation='utf8mb4_general_ci'), comment='接口描述')
    api_doc = db.Column(db.String(255, collation='utf8mb4_general_ci'), nullable=False, default='',comment='接口文档地址')
    integral = db.Column(db.BigInteger, default=0, comment='每次调用积分')
    deleted = db.Column(db.Integer, default=1, comment='逻辑删除 1 未删除 2 已删除')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')

    # 定义索引
    __table_args__ = (
        db.Index('index_host', host),
        db.Index('index_name', name),
        {'comment': 'api信息发布管理表', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )

    def __repr__(self):
        return '<ApiInformation %r>' % self.name
