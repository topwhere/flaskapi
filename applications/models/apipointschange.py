# -*- coding:utf-8 -*-
import datetime
from applications.extensions import db



class ApiPointsChange(db.Model):
    __tablename__ = 'api_points_change'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='自增id')
    api_id = db.Column(db.Integer, default=0, comment='接口id')
    member_points_change_id = db.Column(db.Integer, default=0, comment='积分变更记录id')
    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间/接口调用时间')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')

    # 定义索引
    __table_args__ = (
        db.Index('index_api_id', api_id, mysql_length=10),
        db.Index('index_member_points_change_id', member_points_change_id, mysql_length=10),
        {'comment': 'api积分消费记录表', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}

    )

    def __repr__(self):
        return '<ApiPointsChange %r>' % self.id