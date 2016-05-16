# -*- coding: utf-8 -*-
from flask import current_app, session
from app import socketio, redis, db
from flask_socketio import emit, join_room, leave_room, \
    close_room, rooms, disconnect
from app.models.chat_mod import Message
from datetime import datetime
import time

@socketio.on('connect', namespace='/chat')
def connect():
    emit('system message', {'content': u'成功连接'})

@socketio.on('disconnect', namespace='/chat')
def connect():
    emit('system message', {'content': u'断开连接'})


@socketio.on('join room', namespace='/chat')
def join(message):
    room_id = message['room_id']
    nick_name = session[room_id]
    uid = session['uid']
    join_room(room_id)
    redis.sadd(room_id, room_id + ':' + uid)

    emit('system message', {'content': session[room_id] + u'加入了房间' + message['room_id']}, room=room_id)
    emit('user update', {'flag': 'join', 'uid': uid, 'nick_name': nick_name}, room=room_id)


@socketio.on('leave room', namespace='/chat')
def leave(message):
    room_id = message['room_id']
    nick_name = session[room_id]
    uid = session['uid']
    leave_room(room_id)
    redis.srem(room_id, room_id + ':' + uid)

    emit('system message', {'content': session[room_id] + u'离开了房间' + message['room_id']}, room=room_id)
    emit('user update', {'flag': 'leave', 'uid': uid, 'nick_name': nick_name}, room=room_id)


@socketio.on('user message', namespace='/chat')
def user_message(message):
    room_id = message['room_id']
    message_time = datetime.fromtimestamp(float(message['message_time']))
    content = message['content']
    nick_name = session[room_id]
    serial_number = redis.incr(room_id + ':message_num')
    message = {
        'uid': session['uid'],
        'nick_name': nick_name,
        'message_time': time.mktime(message_time.timetuple()),
        'serial_number': serial_number,
        'content': content
    }
    db.session.add(
        Message(
            message_time=message_time,
            serial_number=serial_number,
            content=content,
            uid=session['uid'],
            nick_name=nick_name,
            room_id=room_id
        )
    )
    db.session.commit()
    emit('user message', message, room=room_id)
