# -*- coding:utf-8 -*-
import datetime
from applications.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import desc, asc


class MemberUser(db.Model):
    __tablename__ = 'member_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='自增id')
    username = db.Column(db.String(64, collation='utf8mb4_general_ci'), default='', comment='用户姓名')
    uuid = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='用户唯一id')
    mobile = db.Column(db.BigInteger, default=0, comment='手机号')
    token = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='用户token（不对外）')
    deleted = db.Column(db.Integer, default=1, comment='逻辑删除 1 未删除 2 已删除')
    status = db.Column(db.Integer, default=1, comment='用户状态 1 正常 2 锁定')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')

    # 定义索引
    __table_args__ = (
    db.Index('index_uuid', uuid, mysql_length=255),
    db.Index('index_token', token, mysql_length=255),
    {'comment': '外部用户表', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )

    def __repr__(self):
        return '<MemberUser %r>' % self.id

