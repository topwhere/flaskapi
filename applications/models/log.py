import datetime
from applications.extensions import db

class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键ID')
    content = db.Column(db.Text(), comment='内容信息')
    user_id = db.Column(db.Integer, comment='操作人id')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')
