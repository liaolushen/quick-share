# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, redirect,\
                    url_for, session
from flask.ext.api import status
from app import app, db
from app.common import generate_random_num_str
from app.models.chat_mod import Room
chat = Blueprint('chat', __name__)


@chat.route('/<room_id>', methods=['GET'])
def index(room_id):
    room = Room.query.get(room_id)
    if room is None:
        return "该房间号不存在"
    if room_id not in session:
        return redirect(url_for('chat.create_name', room_id=room_id))
    data = {
        'room_id': room_id,
        'room_name': room.room_name,
        'user_name': session[room_id]
    }
    return render_template('chat/index.html', data=data)


@chat.route('/<room_id>/create-name', methods=['GET', 'POST'])
def create_name(room_id):
    if request.method == 'GET':
        if room_id in session:
            return redirect(url_for('chat.index', room_id=room_id))
        return render_template('chat/create-name.html', room_id=room_id)
    elif request.method == 'POST':
        session[room_id] = request.form['nick_name']
        return redirect(url_for('chat.index', room_id=room_id))
