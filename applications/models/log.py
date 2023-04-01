import datetime
from applications.extensions import db

class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='����ID')
    content = db.Column(db.Text(), comment='������Ϣ')
    user_id = db.Column(db.Integer, comment='������id')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='����ʱ��')
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='����ʱ��')
