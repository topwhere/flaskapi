# -*- coding:utf-8 -*-
import datetime
from applications.extensions import db

class MemberPointsAccount(db.Model):
    __tablename__ = 'member_points_account'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='自增id')
    uuid = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='用户唯一id')
    historical_points = db.Column(db.BigInteger, default=0, comment='历史充值积分')
    current_points = db.Column(db.BigInteger, default=0, comment='当前积分余额')
    status = db.Column(db.Integer, default=1, comment='账户状态 1 正常 2 锁定')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')

    # 定义索引
    __table_args__ = (
        db.Index('index_uuid', uuid, mysql_length=255),
        {'comment': '用户积分账户表', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )

    def __repr__(self):
        return '<MemberPointsAccount %r>' % self.id