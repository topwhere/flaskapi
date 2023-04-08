from flask import Blueprint

api_ceshi = Blueprint('api_ceshi', __name__, url_prefix='/api/ceshi')


@api_ceshi.route('/')
def index():
    return "这是api/ceshi路由"


