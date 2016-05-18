# -*- coding: utf-8 -*-
from flask import Blueprint, request, session, jsonify
from flask.ext.api import status
import uuid
from app import app, db, redis
from app.models.chat_mod import Room, Message
from app.common import api_format
import time

chat = Blueprint('api_chat', __name__)


@chat.route('/create-name', methods=['POST'])
def create_name():
    """Create nick name for user to join a room
    Add user info to session and redis

    Args:
        nick_name: the user's nick name
        room_id: the id of room

    Returns:
        uid: the user_id to identify the user
        nick_name: the user's nick_name
    """
    json_content = request.get_json()
    if 'uid' not in session:
        session['uid'] = str(uuid.uuid4())
    nick_name = json_content['nick_name']
    room_id = json_content['room_id']
    room = Room.query.get(room_id)
    if room is None:
        session.pop(room_id, None)
        return jsonify(api_format(status.HTTP_404_NOT_FOUND, "no such room"))
    session[room_id] = nick_name
    redis.hmset(room_id + ':' + session['uid'], {'uid': session['uid'], 'nick_name': nick_name})
    return jsonify(api_format(status.HTTP_200_OK, "ok", {'uid': session['uid'], 'nick_name': nick_name}))


@chat.route('/get-name', methods=['GET'])
def get_name():
    room_id = request.values['room_id']
    if 'uid' and room_id in session:
        return jsonify(api_format(status.HTTP_200_OK, "ok", {'uid': session['uid'], 'nick_name': session[room_id]}))
    return jsonify(api_format(status.HTTP_404_NOT_FOUND, "not found"))


@chat.route('/get-room-members', methods=['GET'])
def get_room_members():
    """Get user_id list of the pointed room

    Args:
        room_id: the room that pointed

    Returns:
        room_id: the room that pointed
        user_list: the list of user_id
    """
    room_id = request.values['room_id']
    uid_list = list(redis.smembers(room_id))
    user_list = []
    for uid in uid_list:
        user_list.append(redis.hgetall(uid))
    return jsonify(api_format(status.HTTP_200_OK, "ok", {'room_id': room_id, 'user_list': user_list}))


@chat.route('/get-room-messages', methods=['GET'])
def get_room_messages():
    room_id = request.values['room_id']
    message_num = int(request.values['message_num'])
    result_list = Message.query.filter_by(room_id=room_id).order_by(Message.message_time).limit(message_num).all()
    message_list = []
    for message in result_list:
        message_list.append({
            'serial_number': message.serial_number,
            'uid': message.uid,
            'nick_name': message.nick_name,
            'message_time': time.mktime(message.message_time.timetuple()),
            'content': message.content
        })
    return jsonify(api_format(status.HTTP_200_OK, "ok", {'room_id': room_id, 'message_list': message_list}))
