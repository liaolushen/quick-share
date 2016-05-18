#!/usr/bin/env bash
# 配置脚本

# init
add-apt-repository -y ppa:chris-lea/redis-server
apt-get update
apt-get install -y build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev
apt-get install -y redis-server python-pip python-eventlet

# config
pip install -r requirement.txt
cp config.example.py config.py
