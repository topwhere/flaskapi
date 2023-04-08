import datetime
from applications.extensions import db

class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(10))
    uid = db.Column(db.Integer)
    url = db.Column(db.String(255))
    desc = db.Column(db.Text)
    ip = db.Column(db.String(255))
    success = db.Column(db.Integer)
    user_agent = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)