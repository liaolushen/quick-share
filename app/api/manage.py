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

    q_result = Manager.query.filter_by(email=manager_email, password=manager_password).first()
    if q_result is None:
        return jsonify(api_format(status.HTTP_406_NOT_ACCEPTABLE, "email or password wrong"))
    session['manager_id'] = q_result.id
    return jsonify(api_format(status.HTTP_200_OK, "ok", {'manager_id': q_result.id}))


@manage.route('/create-room', methods=['POST'])
def create_room():
    json_content = request.get_json()
    if 'manager_id' not in session:
        return jsonify(api_format(status.HTTP_406_NOT_ACCEPTABLE, "you are not login"))
    room_name = json_content['room_name']
    description = json_content['description']
    start_time = datetime.fromtimestamp(float(json_content['start_time']))
    end_time = datetime.fromtimestamp(float(json_content['end_time']))
    manager_id = session['manager_id']

    while True:
        new_room_id = generate_random_num_str(6)
        if Room.query.get(new_room_id) is None:
            break
    db.session.add(
        Room(
            room_id=new_room_id,
            room_name=room_name,
            start_time=start_time,
            end_time=end_time,
            description=description,
            manager_id=manager_id
        )
    )
    db.session.commit()
    redis.set(new_room_id + ':message_num', 0)
    return jsonify(api_format(
        status.HTTP_200_OK,
        "ok",
        {
            'room_id': new_room_id,
            'room_name': room_name,
            'start_time': time.mktime(start_time.timetuple()),
            'end_time': time.mktime(end_time.timetuple()),
            'description': description
        }))
