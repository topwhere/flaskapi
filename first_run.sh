pip install -r requirements.txt
# 2 初 始 化 数 据 库

flask init

# 3 创建demo1

flask new --type view --name api/demo1

echo "see: http://127.0.0.1:5000/api/demo1"

# 4 执行 flask run 命令启动项目
flask run
