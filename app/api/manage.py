# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, redirect,\
                    url_for, session, current_app, jsonify
from flask.ext.api import status
from datetime import datetime
from app import app, db
from app.common import generate_random_num_str, api_format
from app.models.chat_mod import Room
from app.models.manage_mod import Manager



manage = Blueprint('api_manage', __name__)


@manage.route('/login', methods=['POST'])
def login():
    manager_email = request.form['manager_email']
    manager_password = request.form['manager_password']

    q_result = Manager.query.filter_by(email=manager_email, password=manager_password).first()
    if q_result is None:
        return jsonify(api_format(status.HTTP_406_NOT_ACCEPTABLE, "email or password wrong"))
    session['manager_id'] = q_result.id
    return jsonify(api_format(status.HTTP_200_OK, "ok", {'manager_id': q_result.id}))


@manage.route('/create-room', methods=['POST'])
def create_room():
    if 'manager_id' not in session:
        return jsonify(api_format(status.HTTP_406_NOT_ACCEPTABLE, "you are not login"))
    room_name = request.form['room_name']
    start_time = datetime.fromtimestamp(float(request.form['start_time']))
    end_time = datetime.fromtimestamp(float(request.form['end_time']))
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
            manager_id=manager_id
        )
    )
    db.session.commit()
    return jsonify(api_format(status.HTTP_200_OK, "ok", {'room_id': new_room_id}))
