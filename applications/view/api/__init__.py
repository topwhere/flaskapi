from flask import Blueprint
from flask_restful import Api

from . import demo
from applications.common.utils.output import output_json

demo_bp = Blueprint('demo', __name__, url_prefix="/v1.0/demo")
demo_api = Api(demo_bp, catch_all_404s=True)
demo_api.representation('application/json')(output_json)

demo_api.add_resource(demo.DemoView, '/',
					 endpoint='Demo')
