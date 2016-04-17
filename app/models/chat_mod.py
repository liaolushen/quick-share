# -*- coding: utf-8 -*-
from app import db


class Room(db.Model):
    """
    文件的存储类
    """
    __tablename__ = 'chat_room'
    id = db.Column(db.String(10), primary_key=True)
    room_name = db.Column(db.String(150), nullable=False)
    room_manager = db.Column(db.String(150), nullable=False)

    def __init__(self, room_id, room_name, room_manager):
        self.id = room_id
        self.room_name = room_name
        self.room_manager = room_manager

    def __repr__(self):
        return 'File(id=%s, room_manager=%s)'\
            % (self.id, self.room_manager)
