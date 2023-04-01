from applications.view.index.index import index_bp

from . import index
from applications.view.index.users import index_users


def register_index_views(app):
    """
    初始化蓝图

    """

    app.register_blueprint(index_users)
    app.register_blueprint(index_bp)
