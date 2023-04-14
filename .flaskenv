# flask配置
FLASK_APP = app.py
FLASK_DEBUG = development
FLASK_DEBUG = 1
FLASK_RUN_HOST = 127.0.0.1
FLASK_RUN_PORT = 5000

# pear admin flask配置
SYSTEM_NAME = UWork

# MySql配置信息
MYSQL_HOST = rm-2zenjcndt98hc2cz17o.mysql.rds.aliyuncs.com
# MYSQL_HOST = dbserver
MYSQL_PORT = 3306
MYSQL_DATABASE = uwork
MYSQL_USERNAME = uwork
MYSQL_PASSWORD = sIhXv5DltiofjQYc

# 密钥配置(记得改)
SECRET_KEY = 'uwork'

# 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_USERNAME = '123@qq.com'
MAIL_PASSWORD = 'XXXXX' # 生成的授权码

# 插件配置
PLUGIN_ENABLE_FOLDERS = ["helloworld"]

# 日志配置
LOGGING_LEVEL = 'DEBUG'
LOGGING_FILE_DIR = '/home/python/logs'
LOGGING_FILE_MAX_BYTES = 300 * 1024 * 1024
LOGGING_FILE_BACKUP = 10