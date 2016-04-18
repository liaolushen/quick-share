# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, redirect,\
                    url_for, session, current_app
from flask.ext.api import status
from app import app, db, socketio
from app.common import generate_random_num_str
from app.models.chat_mod import Room
from flask_socketio import emit, join_room, leave_room, \
    close_room, rooms, disconnect
chat = Blueprint('chat', __name__)


@chat.route('/<room_id>', methods=['GET'])
def index(room_id):
    room = Room.query.get(room_id)
    if room is None:
        return "该房间号不存在"
    if room_id not in current_app.config:
        current_app.config[room_id] = {
            'current_user_num': 0
        }
    if room_id not in session:
        return redirect(url_for('chat.create_name', room_id=room_id))
    data = {
        'room_id': room_id,
        'room_name': room.room_name,
        'nick_name': session[room_id]['nick_name'],
    }
    return render_template('chat/index.html', data=data)


@chat.route('/<room_id>/create-name', methods=['GET', 'POST'])
def create_name(room_id):
    if request.method == 'GET':
        if room_id in session:
            return redirect(url_for('chat.index', room_id=room_id))
        return render_template('chat/create-name.html', room_id=room_id)
    elif request.method == 'POST':
        if room_id not in session:
            session[room_id] = {}
        session[room_id]['nick_name'] = request.form['nick_name']
        return redirect(url_for('chat.index', room_id=room_id))


@socketio.on('connect', namespace='/chat')
def connect():
    emit('new message', {'info': u"成功建立连接！"})


@socketio.on('disconnect', namespace='/chat')
def disconnect():
    print u"有人离开了房间"


@socketio.on('join', namespace='/chat')
def join(message):
    join_room(message['room_id'])
    current_app.config[message['room_id']]['current_user_num'] += 1
    data = {
        'user_num': current_app.config[message['room_id']]['current_user_num'],
        'info': message['nick_name'] + u"加入了房间！"
    }
    emit('user update', data, room=message['room_id'])


@socketio.on('leave', namespace='/chat')
def leave(message):
    leave_room(message['room_id'])
    current_app.config[message['room_id']]['current_user_num'] -= 1
    data = {
        'user_num': current_app.config[message['room_id']]['current_user_num'],
        'info': message['nick_name'] + u"离开了房间！"
    }
    emit('user update', data, room=message['room_id'])


@socketio.on('new message', namespace='/chat')
def new_message(message):
    room_id = message['room_id']
    nick_name = session[room_id]['nick_name']
    print message
    data = {
        'info': nick_name + u":" + message['msg']
    }
    print data
    emit('new message', data, room=room_id)
