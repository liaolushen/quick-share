# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, redirect,\
                    url_for, session, current_app, jsonify
from flask.ext.api import status
from datetime import datetime
from app import app, db, redis
from app.common import generate_random_num_str, api_format
from app.models.chat_mod import Room
from app.models.manage_mod import Manager
import time



manage = Blueprint('api_manage', __name__)


@manage.route('/login', methods=['POST'])
def login():
    json_content = request.get_json()
    manager_email = json_content['manager_email']
    manager_password = json_content['manager_password']

    result_manager = Manager.query.filter_by(email=manager_email, password=manager_password).first()
    if result_manager is None:
        return jsonify(api_format(status.HTTP_406_NOT_ACCEPTABLE, "email or password wrong"))
    session['manager_id'] = result_manager.id
    return jsonify(api_format(
        status.HTTP_200_OK,
        "ok",
        {
            'manager_id': result_manager.id,
            'manager_name': result_manager.name
        }))


@manage.route('/create-room', methods=['POST'])
def create_room():
    if 'manager_id' not in session:
        return jsonify(api_format(status.HTTP_406_NOT_ACCEPTABLE, "you are not login"))
    json_content = request.get_json()
    room_name = json_content['room_name']
    description = json_content['description']
    start_time = int(json_content['start_time'])
    end_time = int(json_content['end_time'])
    manager_id = session['manager_id']

    while True:
        room_id = generate_random_num_str(6)
        if Room.query.get(room_id) is None:
            break
    db.session.add(
        Room(
            room_id=room_id,
            room_name=room_name,
            start_time=start_time,
            end_time=end_time,
            description=description,
            manager_id=manager_id
        )
    )
    db.session.commit()
    redis.set(room_id + ':message_num', 0)
    return jsonify(api_format(
        status.HTTP_200_OK,
        "ok",
        {
            'room_id': room_id,
            'room_name': room_name,
            'start_time': start_time,
            'end_time': end_time,
            'description': description
        }))


@manage.route('/modify-room', methods=['POST'])
def modify_room():
    if 'manager_id' not in session:
        return jsonify(api_format(status.HTTP_406_NOT_ACCEPTABLE, "you are not login"))
    manager_id = session['manager_id']
    json_content = request.get_json()
    room_id = json_content['room_id']
    modified_items = json_content['modified_items']
    result_room = Room.query.filter_by(id=room_id, manager_id=manager_id).first()
    if result_room is None:
        return jsonify(api_format(status.HTTP_404_NOT_FOUND, "room is not existed"))

    for item_name in modified_items:
        if item_name == "start_time" or item_name == "end_time":
            time_item = int(modified_items[item_name])
            setattr(result_room, item_name, time_item)
        else:
            setattr(result_room, item_name, modified_items[item_name])
    db.session.commit()
    return jsonify(api_format(
        status.HTTP_200_OK,
        "ok",
        {
            'room_id': result_room.id,
            'room_name': result_room.name,
            'start_time': result_room.start_time,
            'end_time': result_room.end_time,
            'description': result_room.description
        }))



@manage.route('/get-room-list', methods=['GET'])
def get_room_list():
    if 'manager_id' not in session:
        return jsonify(api_format(status.HTTP_406_NOT_ACCEPTABLE, "you are not login"))
    manager_id = session['manager_id']
    result_list = Room.query.filter_by(manager_id=manager_id).all()
    room_list = []
    for room in result_list:
        room_list.append({
            'room_id': room.id,
            'room_name': room.name,
            'start_time': room.start_time,
            'end_time': room.end_time,
            'description': room.description
        })
    return jsonify(api_format(status.HTTP_200_OK, "ok", {'room_list': room_list}))
