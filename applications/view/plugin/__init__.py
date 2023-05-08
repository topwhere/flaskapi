# -*- coding:utf-8 -*-
from flask import Blueprint
from flask_restful import Api

from . import plugin_tools
from applications.common.utils.output import output_json

plugin_bp = Blueprint('demo', __name__, url_prefix="/v1.0/plugin")
plugin_api = Api(plugin_bp, catch_all_404s=True)
plugin_api.representation('application/json')(output_json)

plugin_api.add_resource(plugin_tools.PluginView, '/data/',
					 endpoint='Plugin')

plugin_api.add_resource(plugin_tools.PluginEnableView, '/enable/',
					 endpoint='PluginEnable')
