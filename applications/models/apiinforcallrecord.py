import datetime
from applications.extensions import db



class ApiInforCallRecord(db.Model):
    __tablename__ = 'api_infor_call_record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='����id')
    api_id = db.Column(db.Integer, default=0, comment='�ӿ�id')
    ip = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='����ip')
    uuid = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='�ӿڵ�����ID')
    create_at = db.Column(db.DateTime, default=datetime.now, comment='����ʱ��/�ӿڵ���ʱ��')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='����ʱ��')

    # ��������
    __table_args__ = (
        db.Index('index_api_id', api_id, mysql_length=10),
        db.Index('index_uuid', uuid, mysql_length=255),
        {'comment': 'api���ü�¼��', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}

    )

    def __repr__(self):
        return '<ApiInforCallRecord %r>' % self.id