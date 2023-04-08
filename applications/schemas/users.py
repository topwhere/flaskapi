from applications.extensions import ma
from marshmallow import fields


class UsersOutSchema(ma.Schema):
    id = fields.Integer()
    username = fields.Str(attribute="username")
    password_hash = fields.Str(attribute="password_hash")
    create_at = fields.DateTime()
    update_at = fields.DateTime()
    enable = fields.Integer()
    delete = fields.Integer()
    realname = fields.Str(attribute="realname")
    avatar = fields.Str(attribute="avatar")
    remark = fields.Method("get_remark")
    dept_id = fields.Integer()

    def get_remark(self, obj):
        if obj.remark != None:
            return obj.remark
        else:
            return "ceshi"
