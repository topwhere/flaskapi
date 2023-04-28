import datetime
from applications.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import desc, asc


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

    """
            ��ȡһ��
            @param set filters ��ѯ����
            @param obj order ����
            @param tuple field �ֶ�
            @return dict
        """

    def getOne(self, filters, order='id desc', field=()):
        res = db.query(self).filter(*filters)
        order = order.split(' ')
        if order[1] == 'desc':
            res = res.order_by(desc(order[0])).first()
        else:
            res = res.order_by(asc(order[0])).first()
        if res == None:
            return None
        if not field:
            res = res.to_dict()
        else:
            res = res.to_dict(only=field)
        return res
        # ��������

    # ��������
    @staticmethod
    def set_password(password):
        return generate_password_hash(password)

    # У������
    @staticmethod
    def check_password(hash_password, password):
        return check_password_hash(hash_password, password)

    # ��ȡ�û���Ϣ
    @staticmethod
    def get(id):
        return db.query(MemberUser).filter_by(id=id).first()

    # �����û�
    def add(self, user):
        db.add(user)
        return True

    # ����idɾ���û�
    def delete(self, id):
        db.query(MemberUser).filter_by(id=id).update({'deleted': 2})
        return db.commit()