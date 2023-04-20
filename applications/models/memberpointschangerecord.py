import datetime
from applications.extensions import db

class MemberPointsChangeRecord(db.Model):
    __tablename__ = 'member_points_change_record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='����id')
    uuid = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='�û�uuid')
    account_id = db.Column(db.Integer, default=0, comment='�˻�id')
    points = db.Column(db.BigInteger, default=0, comment='���ֶ��')
    type = db.Column(db.Boolean, default=True, comment='�������� 1 ��-��ֵ���� 2 ��-���ѻ��� 3 ��-���ͻ���')
    create_at = db.Column(db.DateTime, default=datetime.now, comment='����ʱ��')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='����ʱ��')

    # ��������
    __table_args__ = (
        db.Index('idx_uuid', uuid, mysql_length=255),
        {'comment': '�û��˻����ֱ����¼��', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )

    def __repr__(self):
        return '<MemberPointsChangeRecord %r>' % self.id