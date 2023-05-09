# -*- coding: utf-8 -*-
import os
import json
import traceback
import importlib

from flask import current_app
from flask_restful import Resource

from flask import request, escape
from applications.common.utils.http import table_api, fail_api, success_api

# from applications.common.utils.rights import authorize
PLUGIN_ENABLE_FOLDERS = []

print(current_app.config.get('PLUGIN_ENABLE_FOLDERS'))


# current_app.redis_cluster
# current_app.xxx 全局对象


def register_plugin_views(app):
	global PLUGIN_ENABLE_FOLDERS
	# app.register_blueprint(plugin_bp)
	# 载入插件过程
	# plugin_folder 配置的是插件的文件夹名
	PLUGIN_ENABLE_FOLDERS = json.loads(app.config['PLUGIN_ENABLE_FOLDERS'])
	for plugin_folder in PLUGIN_ENABLE_FOLDERS:
		plugin_info = {}
		try:
			with open("plugins/" + plugin_folder + "/__init__.json", "r", encoding='utf-8') as f:
				plugin_info = json.loads(f.read())
			# 初始化完成事件
			try:
				getattr(importlib.import_module('plugins.' + plugin_folder), "event_init")(app)
			except AttributeError:  # 没有插件启用事件就不调用
				pass
			except BaseException as error:
				return fail_api(msg="Crash a error! Info: " + str(error))
			print(f" * Plugin: Loaded plugin: {plugin_info['plugin_name']} .")
		except BaseException as e:
			info = f" * Plugin: Crash a error when loading {plugin_info['plugin_name'] if len(plugin_info) != 0 else 'plugin'} :" + "\n"
			info += 'str(Exception):\t' + str(Exception) + "\n"
			info += 'str(e):\t\t' + str(e) + "\n"
			info += 'repr(e):\t' + repr(e) + "\n"
			info += 'traceback.format_exc():\n%s' + traceback.format_exc()


class PluginView(Resource):

	def get(self):
		"""请求插件数据"""
		plugin_name = escape(request.args.get("plugin_name"))
		all_plugins = []
		count = 0
		for filename in os.listdir("plugins"):
			try:
				with open("plugins/" + filename + "/__init__.json", "r", encoding='utf-8') as f:
					info = json.loads(f.read())

					if plugin_name is None:
						if info['plugin_name'].find(plugin_name) == -1:
							continue

					all_plugins.append(
						{
							"plugin_name": info["plugin_name"],
							"plugin_version": info["plugin_version"],
							"plugin_description": info["plugin_description"],
							"plugin_folder_name": filename,
							"enable": "1" if filename in PLUGIN_ENABLE_FOLDERS else "0"
						}
					)
				count += 1
			except BaseException as error:
				print(filename, error)
				continue
		data = table_api(data=all_plugins, count=count)
		return {"data": data}, 200


class PluginEnableView(Resource):
	def put(self):
		# 校验需要修改
		plugin_folder_name = request.json.get('plugin_folder_name')
		if plugin_folder_name:
			try:
				if plugin_folder_name not in PLUGIN_ENABLE_FOLDERS:
					PLUGIN_ENABLE_FOLDERS.append(plugin_folder_name)
					with open(".flaskenv", "r", encoding='utf-8') as f:
						flaskenv = f.read()  # type: str
					pos1 = flaskenv.find("PLUGIN_ENABLE_FOLDERS")
					pos2 = flaskenv.find("\n", pos1)
					with open(".flaskenv", "w", encoding='utf-8') as f:
						if pos2 == -1:
							f.write(flaskenv[:pos1] + "PLUGIN_ENABLE_FOLDERS = " + json.dumps(PLUGIN_ENABLE_FOLDERS))
						else:
							f.write(
								flaskenv[:pos1] + "PLUGIN_ENABLE_FOLDERS = " + json.dumps(
									PLUGIN_ENABLE_FOLDERS) + flaskenv[
															 pos2:])
					# 启用插件事件
					try:
						getattr(importlib.import_module('plugins.' + plugin_folder_name), "event_enable")()
					except AttributeError:  # 没有插件启用事件就不调用
						pass
					except BaseException as error:
						data = fail_api(msg="Crash a error! Info: " + str(error))
						return {"data": data, "code": 0}, 400

			except BaseException as error:
				data = fail_api(msg="Crash a error! Info: " + str(error))
				return {"data": data, "code": 0}, 400

			data = success_api(msg="启用成功，要使修改生效需要重启程序。")

		else:
			data = fail_api(msg="数据错误")

		return {"data": data}, 200