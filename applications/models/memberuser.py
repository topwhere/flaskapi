import datetime
from applications.extensions import db


class MemberUser(db.Model):
    __tablename__ = 'member_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='����id')
    username = db.Column(db.String(64, collation='utf8mb4_general_ci'), default='', comment='�û�����')
    uuid = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='�û�Ψһid')
    token = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='�û�token�������⣩')
    deleted = db.Column(db.Boolean, default=True, comment='�߼�ɾ�� 1 δɾ�� 2 ��ɾ��')
    status = db.Column(db.Boolean, default=True, comment='�û�״̬ 1 ���� 2 ����')
    create_at = db.Column(db.DateTime, default=datetime.now, comment='����ʱ��')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='����ʱ��')

    # ��������
    __table_args__ = (
    db.Index('index_uuid', uuid, mysql_length=255),
    db.Index('index_token', token, mysql_length=255),
    {'comment': '�ⲿ�û���', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )

    def __repr__(self):
        return '<MemberUser %r>' % self.id