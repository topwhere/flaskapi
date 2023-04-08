from flask import Blueprint, request
from applications.common.utils.validate import str_escape
from applications.common import curd
from applications.common.utils.http import fail_api, success_api,data_api
from applications.extensions import db
from applications.models import Users, Role
from applications.schemas import UsersOutSchema

api_users = Blueprint('api_users', __name__, url_prefix='/api/users')


@api_users.route('/')
def index():
    return "这是api/users路由"



@api_users.get('/getusers/<int:userid>')
# @authorize("admin:user:delete", log=True)
def getusers(userid):
    users = curd.get_one_by_id(Users, userid)
    print(1)
    print(users.realname)
    print(type(users))
    type(users)
    print(2)
    # data = curd.model_to_dicts(schema=UsersOutSchema, data=users)

    users_schema = UsersOutSchema(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    print(3)

    output = users_schema.dump(users)  # 生成可序列化对象
    print(4)
    for i in output:
       print(i)
       print(5)

    print(output)
    print(6)
    return data_api(200,curd.model_to_dicts(schema=UsersOutSchema, data=users))


@api_users.post('/addUser')
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
@api_users.delete('/delete/<int:id>')
# @authorize("admin:user:delete", log=True)
def delete(id):
    user = Users.query.filter_by(id=id).first()
    user.role = []

    res = Users.query.filter_by(id=id).delete()
    db.session.commit()
    if not res:
        return fail_api(msg="删除失败")
    return success_api(msg="删除成功")