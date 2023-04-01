from applications.extensions import ma
from marshmallow import fields


class UsersOutSchema(ma.Schema):
    id = fields.Integer()
    username = fields.Str(attribute="username")
    realname = fields.Str(attribute="realname")
    create_at = fields.DateTime()
    update_at = fields.DateTime()
