# -*- coding:utf-8 -*-
import datetime
from applications.extensions import db


class ApiInforChangeRecord(db.Model):
    __tablename__ = 'api_infor_change_record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='自增id')
    api_id = db.Column(db.Integer, default=0, comment='接口id')
    edit_mark = db.Column(db.Text(collation='utf8mb4_general_ci'), comment='变更口描述')
    edit_uuid = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='接口修改人uuid')
    new_info = db.Column(db.Text(collation='utf8mb4_general_ci'), comment='接口修改前信息')
    old_info = db.Column(db.Text(collation='utf8mb4_general_ci'), comment='接口修改后信息')
    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')

    # 定义索引
    __table_args__ = (
        db.Index('index_api_id', api_id, mysql_length=10),
        {'comment': 'api变更记录表', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )

    def __repr__(self):
        return '<ApiInforChangeRecord %r>' % self.id
