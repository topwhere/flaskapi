import datetime
from applications.extensions import db

class Demo(db.Model):
    __tablename__ = 'demo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10))
    status = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')
