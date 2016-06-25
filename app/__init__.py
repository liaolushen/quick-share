# -*- coding: utf-8 -*-
# Import flask and template operators
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
from flask_socketio import SocketIO
from flask_redis import Redis

import eventlet
async_mode = "eventlet"
eventlet.monkey_patch()

# Define the WSGI application object
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

socketio = SocketIO(app, async_mode=async_mode)
db = SQLAlchemy(app)
redis = Redis(app)
cors = CORS(app, resources={r"*": {"origins": "*"}}, supports_credentials=True)


import views, socket, api

db.create_all()
db.session.commit()

# 添加测试数据
import test_data
