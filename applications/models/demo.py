import datetime
from applications.extensions import db

class Demo(db.Model):
    __tablename__ = 'demo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), comment='测试描述')
    status = db.Column(db.Integer, comment='状态(1开启,0关闭)')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')

