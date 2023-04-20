import datetime
from applications.extensions import db


class ApiInforChangeRecord(db.Model):
    __tablename__ = 'api_infor_change_record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='����id')
    api_id = db.Column(db.Integer, default=0, comment='�ӿ�id')
    edit_mark = db.Column(db.Text(collation='utf8mb4_general_ci'), comment='���������')
    edit_uuid = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='�ӿ��޸���uuid')
    new_info = db.Column(db.Text(collation='utf8mb4_general_ci'), comment='�ӿ��޸�ǰ��Ϣ')
    old_info = db.Column(db.Text(collation='utf8mb4_general_ci'), comment='�ӿ��޸ĺ���Ϣ')
    create_at = db.Column(db.DateTime, default=datetime.now, comment='����ʱ��')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='����ʱ��')

    # ��������
    __table_args__ = (
        db.Index('index_api_id', api_id, mysql_length=10),
        {'comment': 'api�����¼��', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )

    def __repr__(self):
        return '<ApiInforChangeRecord %r>' % self.id
