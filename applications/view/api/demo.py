from flask import Blueprint
from applications.common.utils.http import fail_api, success_api,data_api
from applications.common.curd import model_to_dicts,get_one_by_id,auto_model_jsonify
from applications.common.utils.rights import authorize
from applications.extensions import db
from applications.models import Demo
from applications.schemas import DemoOutSchema





api_demo = Blueprint('api_demo', __name__, url_prefix='/api/demo')


@api_demo.route('/')
def index():
    return "这是api/demo路由"

@api_demo.get('/addDemo')
def addDemo():
    # req_json = request.json
    title = "123"

    if not title or not title or not title:
        return fail_api(msg="title不得为空")

    if bool(Demo.query.filter_by(title=title).count()):
        return fail_api(msg="title已经存在")
    user = Demo(
        title=title,
        status=1,
    )
    db.session.add(user)
    db.session.commit()
    return success_api(msg="增加成功")


@api_demo.get('/editDemo')
def editDemo():
    # req_json = request.json
    # id = str_escape(req_json.get("id"))
    # title = str_escape(req_json.get("title"))
    id = 3
    title = "ceshi"
    if not id or not id or not id:
        return fail_api(msg="id不得为空")
    if not title or not title or not title:
        return fail_api(msg="title不得为空")
    res = Demo.query.filter_by(id=id).update({'title': title})
    db.session.commit()
    if not res:
        return fail_api(msg="编辑失败")
    return success_api(msg="编辑成功")


@api_demo.get('/delDemo/<int:id>')
# http://127.0.0.1:5000/api/demo/delDemo/1
def delDemo(id):
    demoData = Demo.query.filter_by(id=id).first()

    if not demoData:
        return fail_api(msg="不存在有效数据")

    res = demoData.query.filter_by(id=id).delete()
    db.session.commit()

    if not res:
        return fail_api(msg="删除失败")
    return success_api(msg="删除成功")




# 批量查询demo1
@api_demo.get('/getDemo1')
def getDemo1():
    # req_json = request.json
    # id = str_escape(req_json.get("id"))
    id = "4"
    if not id or not id or not id:
        return fail_api(msg="id不得为空")

    demoData = Demo.query.filter_by(id=id).all()
    data = auto_model_jsonify(demoData,Demo)

    return data_api(200,data)

# 批量查询demo2
@api_demo.get('/getDemo2')
def getDemo2():
    # req_json = request.json
    # id = str_escape(req_json.get("id"))

    id = "4"

    if not id or not id or not id:
        return fail_api(msg="id不得为空")

    demoData = Demo.query.filter_by(id=id).all()
    data = model_to_dicts(schema=DemoOutSchema, data=demoData)

    return data_api(200,data)



# 单条查询demo1
@api_demo.get('/getDemo3')
def getDemo3():
    # req_json = request.json
    # id = str_escape(req_json.get("id"))

    id = "4"

    if not id or not id or not id:
        return fail_api(msg="id不得为空")


    demoData = Demo.query.filter_by(id=id).first()
    if not demoData:
        return fail_api(msg="不存在有效数据")
    data = {
        "title": demoData.title,
        "status": demoData.status
    }

    return data_api(200,data)





