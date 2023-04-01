from applications.view.admin import register_admin_views
from applications.view.index import register_index_views
from applications.view.plugin import register_plugin_views

def init_view(app):
    register_admin_views(app)
    register_index_views(app)
    register_plugin_views(app)
