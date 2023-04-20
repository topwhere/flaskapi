import datetime
from applications.extensions import db



class ApiPointsChange(db.Model):
    __tablename__ = 'api_points_change'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='����id')
    api_id = db.Column(db.Integer, default=0, comment='�ӿ�id')
    member_points_change_id = db.Column(db.Integer, default=0, comment='���ֱ����¼id')
    create_at = db.Column(db.DateTime, default=datetime.now, comment='����ʱ��/�ӿڵ���ʱ��')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='����ʱ��')

    # ��������
    __table_args__ = (
        db.Index('index_api_id', api_id, mysql_length=10),
        db.Index('index_member_points_change_id', member_points_change_id, mysql_length=10),
        {'comment': 'api�������Ѽ�¼��', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}

    )

    def __repr__(self):
        return '<ApiPointsChange %r>' % self.id