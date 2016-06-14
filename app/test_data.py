# -*- coding: utf-8 -*-
import datetime, uuid
from . import db, redis
from flask import session
from models.manage_mod import Manager
from models.chat_mod import Room, Message
from flask_socketio import join_room

# 清空redis
redis.flushall()

# 添加管理员
db.session.add(
    Manager(
        manager_email="123456@qq.com",
        manager_password="123456",
        manager_name=u"御坂美琴"
    )
)

# 添加房间
db.session.add(
    Room(
        room_id='123456',
        room_name=u'御坂美琴の粉丝团1',
        start_time=1463939795682,
        end_time=1463939797682,
        description=u'御坂美琴',
        manager_id=1
    )
)

db.session.add(
    Room(
        room_id='123457',
        room_name=u'御坂美琴の粉丝团2',
        start_time=1463939795682,
        end_time=1463939895682,
        description=u'御坂美琴',
        manager_id=1
    )
)
db.session.commit()
redis.set('123456:message_num', 0)
redis.set('123457:message_num', 0)

# 添加用户1
uid = str(uuid.uuid4())
nick_name = u'开哥'
room_id = '123456'
redis.sadd(room_id, room_id + ':' + uid)
redis.hmset(room_id + ':' + uid, {'uid': uid, 'nick_name': nick_name})

# 用户1说话
db.session.add(
    Message(
        message_time=1463939795782,
        serial_number=redis.incr(room_id + ':message_num'),
        content=u'大家好，我是开哥',
        uid=uid,
        nick_name=nick_name,
        room_id=room_id
    )
)

db.session.add(
    Message(
        message_time=1463939796782,
        serial_number=redis.incr(room_id + ':message_num'),
        content=u'欢迎大家找我啪啪啪',
        uid=uid,
        nick_name=nick_name,
        room_id=room_id
    )
)

# 添加用户2
uid = str(uuid.uuid4())
nick_name = u'御姐'
room_id = '123456'
redis.sadd(room_id, room_id + ':' + uid)
redis.hmset(room_id + ':' + uid, {'uid': uid, 'nick_name': nick_name})

# 用户1说话
db.session.add(
    Message(
        message_time=1463939798782,
        serial_number=redis.incr(room_id + ':message_num'),
        content=u'大家好，我是御姐',
        uid=uid,
        nick_name=nick_name,
        room_id=room_id
    )
)

db.session.add(
    Message(
        message_time=1463939799782,
        serial_number=redis.incr(room_id + ':message_num'),
        content=u'我要和开哥啪啪啪',
        uid=uid,
        nick_name=nick_name,
        room_id=room_id
    )
)

db.session.commit()
