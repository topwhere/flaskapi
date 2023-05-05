from flask_restful import Resource

from applications.common.utils.decorators import login_required


class AuthorizationTestView(Resource):
	method_decorators = [login_required]

	def get(self):
		return {"message": "登陆后获取数据"}, 200
