# -*- coding:utf-8 -*-
import datetime
from applications.extensions import db

class MemberPointsChangeRecord(db.Model):
    __tablename__ = 'member_points_change_record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='自增id')
    uuid = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='用户uuid')
    account_id = db.Column(db.Integer, default=0, comment='账户id')
    points = db.Column(db.BigInteger, default=0, comment='积分额度')
    type = db.Column(db.Integer, default=1, comment='积分类型 1 增-充值积分 2 减-消费积分 3 增-赠送积分')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')

    # 定义索引
    __table_args__ = (
        db.Index('idx_uuid', uuid, mysql_length=255),
        {'comment': '用户账户积分变更记录表', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )

    def __repr__(self):
        return '<MemberPointsChangeRecord %r>' % self.id