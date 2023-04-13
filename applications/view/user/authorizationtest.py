from flask import Blueprint
from flask_restful import Api,Resource

from applications.common.utils.output import output_json
from applications.common.utils.decorators import login_required

user_authorizationtest = Blueprint('user_authorizationtest', __name__, url_prefix='/user/authorizationtest')


user_api = Api(user_authorizationtest, catch_all_404s=True)
user_api.representation('application/json')(output_json)


class AuthorizationTestView(Resource):
    method_decorators = [login_required]

    def get(self):
        return {"message": "登陆后获取数据"}, 200

user_api.add_resource(AuthorizationTestView, '/test', endpoint='AuthorizationTest')