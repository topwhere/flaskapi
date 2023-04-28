import datetime
from applications.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import desc, asc


class MemberUser(db.Model):
    __tablename__ = 'member_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='自增id')
    username = db.Column(db.String(64, collation='utf8mb4_general_ci'), default='', comment='用户姓名')
    uuid = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='用户唯一id')
    token = db.Column(db.String(255, collation='utf8mb4_general_ci'), default='', comment='用户token（不对外）')
    deleted = db.Column(db.Boolean, default=True, comment='逻辑删除 1 未删除 2 已删除')
    status = db.Column(db.Boolean, default=True, comment='用户状态 1 正常 2 锁定')
    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')

    # 定义索引
    __table_args__ = (
    db.Index('index_uuid', uuid, mysql_length=255),
    db.Index('index_token', token, mysql_length=255),
    {'comment': '外部用户表', 'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )

    def __repr__(self):
        return '<MemberUser %r>' % self.id

    """
            获取一条
            @param set filters 查询条件
            @param obj order 排序
            @param tuple field 字段
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
        # 设置密码

    # 设置密码
    @staticmethod
    def set_password(password):
        return generate_password_hash(password)

    # 校验密码
    @staticmethod
    def check_password(hash_password, password):
        return check_password_hash(hash_password, password)

    # 获取用户信息
    @staticmethod
    def get(id):
        return db.query(MemberUser).filter_by(id=id).first()

    # 增加用户
    def add(self, user):
        db.add(user)
        return True

    # 根据id删除用户
    def delete(self, id):
        db.query(MemberUser).filter_by(id=id).update({'deleted': 2})
        return db.commit()