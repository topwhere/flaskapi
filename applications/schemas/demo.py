# -*- coding:utf-8 -*-
from applications.extensions import ma
from marshmallow import fields,validate


class DemoOutSchema(ma.Schema):
    id = fields.Integer()
    title = fields.Str()
    status = fields.Str(validate=validate.OneOf(["0", "1"]))
    create_at = fields.DateTime()
    update_at = fields.DateTime()
