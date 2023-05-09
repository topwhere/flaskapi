# -*- coding:utf-8 -*-
import os
from flask import Flask

from applications.common.script import init_script
from applications.extensions import init_plugs
# from applications.extensions.init_logger import init_logger
from applications.configs import config


def create_app(config_name=None):
	app = Flask(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

	if not config_name:
		# 尝试从本地环境中读取
		config_name = os.getenv('FLASK_CONFIG', 'development')

	# 引入数据库配置
	app.config.from_object(config[config_name])

	# 注册url转换器
	from applications.common.utils.converters import register_converters
	register_converters(app)

	# 注册各种插件
	init_plugs(app)

	# 注册命令
	init_script(app)

	if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
		logo()

	# 注册蓝图
	from applications.view.user import user_bp
	app.register_blueprint(user_bp)
	from applications.view.api import demo_bp
	app.register_blueprint(demo_bp)
	# from applications.view.plugin import plugin_bp
	# app.register_blueprint(plugin_bp)

	return app


def logo():
	print('''
    WelCome To Uwork
    ''')
