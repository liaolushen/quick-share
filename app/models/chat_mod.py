# -*- coding: utf-8 -*-
from app import db


class Room(db.Model):
    """
    聊天室类
    """
    __tablename__ = 'chat_room'
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    start_time = db.Column(db.Integer)
    end_time = db.Column(db.Integer)
    description = db.Column(db.Text)
    manager_id = db.Column(db.Integer, db.ForeignKey('manager.id'))

    def __init__(self, room_id, room_name, start_time, end_time, description, manager_id):
        self.id = room_id
        self.name = room_name
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.manager_id = manager_id

    def __repr__(self):
        return 'File(id=%s, room_manager=%s)'\
            % (self.id, self.room_manager)


class Message(db.Model):
    """
    聊天记录类
    """
    __tablename__ = 'chat_message'
    id = db.Column(db.Integer, primary_key=True)
    message_time = db.Column(db.Integer)
    serial_number = db.Column(db.Integer)
    content = db.Column(db.Text)
    uid = db.Column(db.String(80))
    nick_name = db.Column(db.String(100))
    room_id = db.Column(db.String(10), db.ForeignKey('chat_room.id'))

    def __init__(self, message_time, serial_number, content, uid, nick_name, room_id):
        self.message_time = message_time
        self.serial_number = serial_number
        self.content = content
        self.uid = uid
        self.nick_name = nick_name
        self.room_id = room_id

    def __repr__(self):
        return 'Message(id=%d, uid=%s, room_id=%s)'\
            % (self.id, self.uid, self.room_id)
