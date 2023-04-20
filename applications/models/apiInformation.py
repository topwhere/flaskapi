import datetime
from applications.extensions import db


class ApiInformation(db.Model):
    __tablename__ = 'api_information'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='����id')
    host = db.Column(db.String(255, collation='utf8mb4_general_ci'), nullable=False, default='', comment='�ӿڵ�ַ')
    name = db.Column(db.String(255, collation='utf8mb4_general_ci'), nullable=False, default='', comment='�ӿ�����')
    api_mark = db.Column(db.Text(collation='utf8mb4_general_ci'), comment='�ӿ�����')
    api_doc = db.Column(db.String(255, collation='utf8mb4_general_ci'), nullable=False, default='',comment='�ӿ��ĵ���ַ')
    integral = db.Column(db.BigInteger, default=0, comment='ÿ�ε��û���')
    deleted = db.Column(db.Boolean, default=True, comment='�߼�ɾ�� 1 δɾ�� 2 ��ɾ��')
    create_at = db.Column(db.DateTime, default=datetime.now, comment='����ʱ��')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='����ʱ��')

    # ��������
    __table_args__ = (
        db.Index('index_host', host),
        db.Index('index_name', name),
        {'comment': 'api��Ϣ���������', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )

    def __repr__(self):
        return '<ApiInformation %r>' % self.name