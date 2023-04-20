import datetime
from applications.extensions import db

class MemberPointsAccount(db.Model):
    __tablename__ = 'member_points_account'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='����id')
    uuid = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='�û�Ψһid')
    historical_points = db.Column(db.BigInteger, default=0, comment='��ʷ��ֵ����')
    current_points = db.Column(db.BigInteger, default=0, comment='��ǰ�������')
    status = db.Column(db.Boolean, default=True, comment='�˻�״̬ 1 ���� 2 ����')
    create_at = db.Column(db.DateTime, default=datetime.now, comment='����ʱ��')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='����ʱ��')

    # ��������
    __table_args__ = (
        db.Index('index_uuid', uuid, mysql_length=255),
        {'comment': '�û������˻���', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )

    def __repr__(self):
        return '<MemberPointsAccount %r>' % self.id