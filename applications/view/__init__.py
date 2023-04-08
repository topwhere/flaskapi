from applications.view.api import register_api_views
from applications.view.plugin import register_plugin_views

def init_view(app):
    register_api_views(app)
    register_plugin_views(app)
