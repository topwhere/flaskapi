from flask import  Blueprint
from applications.common.utils.http import success_api

index_bp = Blueprint('Index', __name__, url_prefix='/')


@index_bp.route('/')
def index():

    return success_api("ok")

