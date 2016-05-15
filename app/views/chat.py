# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, redirect,\
                    url_for, session, current_app, abort
from flask.ext.api import status
from app import app, db, socketio
from app.common import generate_random_num_str
from app.models.chat_mod import Room
chat = Blueprint('view_chat', __name__)


@chat.route('/<room_id>', methods=['GET'])
def index(room_id):
    room = Room.query.get(room_id)
    if room is None:
        abort(404)
    if room_id not in session:
        return redirect(url_for('view_chat.create_name', room_id=room_id))
    return render_template('chat/index.html', room_id=room_id)


@chat.route('/<room_id>/create-name', methods=['GET'])
def create_name(room_id):
    room = Room.query.get(room_id)
    if room is None:
        abort(404)
    if room_id in session:
        return redirect(url_for('view_chat.index', room_id=room_id))
    return render_template('chat/create-name.html', room_id=room_id)
