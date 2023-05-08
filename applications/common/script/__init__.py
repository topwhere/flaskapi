# -*- coding:utf-8 -*-
import os


from applications.common.script.initdb import init_db
from applications.common.script.newmodular.new import NewViewModular


def init_script(app):
    def init():
        init_db()


    @app.cli.command()
    def new(type,name):
        if type == 'view':
            if name.count('/') > 1:
                print("目前只支持二级目录，多级目录需要蓝图嵌套，本命令暂不支持，请手动创建")
                quit()
            if type == "view" and os.path.exists(f"applications/view/{name}.py"):
                print(f'已经存在视图模块{name}.py')
                quit()
            NewViewModular(name=name).new_view()