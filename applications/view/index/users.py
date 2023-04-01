from flask import Blueprint, request
from applications.common.utils.validate import str_escape
from applications.common import curd
from applications.common.utils.http import fail_api, success_api,data_api
from applications.extensions import db
from applications.models import Users, Role
from applications.common.curd import model_to_dicts
from applications.schemas import UsersOutSchema


index_users = Blueprint('index_users', __name__, url_prefix='/index/users')


@index_users.route('/')
def index():
    return "这是index/users路由"



@index_users.get('/getusers/<int:userid>')
# @authorize("admin:user:delete", log=True)
def getusers(userid):
    user = curd.get_one_by_id(Users, userid)
    print(1)
    print(user.realname)
    print(type(user))
    type(user)
    print(2)
    data = curd.model_to_dicts(schema=UsersOutSchema, data=user)
    print(data)
    print(3)
    return data_api(200,curd.model_to_dicts(schema=UsersOutSchema, data=user))


@index_users.post('/addUser')
# @authorize("admin:user:add", log=True)
def addUser():
    req_json = request.json
    #
    a = req_json.get("roleIds")
    username = str_escape(req_json.get('username'))
    real_name = str_escape(req_json.get('realName'))
    password = str_escape(req_json.get('password'))
    role_ids = a.split(',')

    username  = "demo"
    real_name = "demoName"
    password  = "123"
    role_ids  = [1, 2, 3]
    # if not username or not real_name or not password:
    #     return fail_api(msg="账号姓名密码不得为空")
    #
    # if bool(User.query.filter_by(username=username).count()):
    #     return fail_api(msg="用户已经存在")

    user = Users(username, real_name)
    user.set_password(password)
    db.session.add(user)
    roles = Role.query.filter(Role.id.in_(role_ids)).all()
    for r in roles:
        user.role.append(r)
    db.session.commit()
    return success_api(msg="增加成功")


# 删除用户
@index_users.delete('/delete/<int:id>')
# @authorize("admin:user:delete", log=True)
def delete(id):
    user = Users.query.filter_by(id=id).first()
    user.role = []

    res = Users.query.filter_by(id=id).delete()
    db.session.commit()
    if not res:
        return fail_api(msg="删除失败")
    return success_api(msg="删除成功")