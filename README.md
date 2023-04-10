<div align="center">
<br/>
<br/>
  <h1 align="center">
    Uwork
  </h1>
  <h4>
    Uwork 快 速 开 发 平 台
  </h4> 

  [预 览](http://www.baidu.com)   |   [官 网](http://www.baidu.com/)   |   [文档](docs/detail.md)

</div>


#### 项目简介
略

**[main分支版本 ](https://xxx/tree/main/)**

main 分支为主分支。

**[其他分支版本](https://xxx/other/)**

略


####  现有功能

暂无

####  项目结构

```
uWork
├─applications    # 应用
│  ├─common         # 配置文件
│  │  ├─  script    # 定义好的flask命令（目前包括初始化数据库，快捷创建操作方法文件）
│  │  ├─  tasks     # 功能未知 ？
│  │  ├─  utils     # 组件（如邮件，上传，返回定义，校验等）
│  │  ├─  curd.py   # 数据库 curd 操作，针对 model
│  │  ├─  log.py    # 记录 log 的公共方法
│  │  └─  helper.py # orm 构造器
│  ├─configs      # 配置文件
│  │  └─ config.py  # 配置文件对象
│  ├─extensions  # 注册插件
│  ├─models  # 数据 model 模型
│  ├─schemas # 数据 schemas 类
│  ├─static  # 静态资源文件(暂无)
│  ├─templates  # 静态模板文件(暂无)
│  └─views  # 视图部分(暂无)
├─docs  # 文档说明
├─migrations  # 迁移文件记录（暂未应用，待开发）
├─requirement  # 依赖文件目录（用来安装相关依赖）
└─.env # 项目的配置文件

```

#### 项目安装

```bash
# 下 载
git clone xxxx

# 配 置
.flaskenv

```

#### 修改配置

```python
.env
# MySql配置信息
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

# Redis 配置
# REDIS_HOST=127.0.0.1
# REDIS_PORT=6379

# 密钥配置(记得改)
SECRET_KEY = 'uwork'

# 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_USERNAME = '123@qq.com'
MAIL_PASSWORD = 'XXXXX' # 生成的授权码

# 插件配置
PLUGIN_ENABLE_FOLDERS = ["helloworld"]
```

#### 运行项目

```bash
# 1 安 装 依 赖 包
pip install -r requirements.txt
# 2 初 始 化 数 据 库

flask init

# 3 执行 flask run 命令启动项目

flask run


```



#### 命令行创建视图

```bash
# 示例

flask new --type view --name api/demo1


# 访问http://127.0.0.1:5000/api/demo1
```

