#!/usr/bin/env bash
# 运行脚本

# 清空redis缓存数据库
redis-cli flushall

# 运行应用服务器
rm -rf app/static
rm app/templates/index.html
cp -r html/dist/static app/
 cp html/dist/index.html app/templates/index.html
python run.py
