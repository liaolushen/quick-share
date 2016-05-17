#!/usr/bin/env bash
# 运行脚本

# 清空redis缓存数据库
redis-cli flushall

# 运行应用服务器
python run.py
