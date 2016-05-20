# -*- coding: utf-8 -*-
# Import flask and template operators
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
from flask_socketio import SocketIO
from flask_redis import Redis
import datetime

# Define the WSGI application object
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

socketio = SocketIO(app)
db = SQLAlchemy(app)
redis = Redis(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})


import views, socket, api

db.create_all()

# add default manager for test
from models.manage_mod import Manager
from models.chat_mod import Room
db.session.add(
    Manager(
        manager_email="123456@qq.com",
        manager_password="123456",
        manager_name=u"御坂美琴"
    )
)

db.session.add(
    Room(
        room_id='123456',
        room_name=u'御坂美琴',
        start_time=datetime.datetime(2015, 6, 12),
        end_time=datetime.datetime(2015, 7, 21),
        description=u'御坂美琴',
        manager_id=1
    )
)

db.session.add(
    Room(
        room_id='123457',
        room_name=u'御坂美琴',
        start_time=datetime.datetime(2015, 6, 12),
        end_time=datetime.datetime(2015, 7, 21),
        description=u'御坂美琴',
        manager_id=1
    )
)

db.session.commit()
