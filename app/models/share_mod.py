# -*- coding: utf-8 -*-
from app import db
from app.common import get_file_format


class File(db.Model):
    """
    文件的存储类
    """
    __tablename__ = 'share_file'
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(150), nullable=False)
    file_format = db.Column(db.String(50), nullable=False)
    file_size = db.Column(db.Integer)
    room_id = db.Column(db.String(10))

    def __init__(self, file_name, file_format, file_size, room_id):
        self.file_name = file_name
        self.file_format = file_format
        self.file_size = file_size
        self.room_id = room_id

    def __repr__(self):
        return 'File(id=%d, room_id=%s)'\
            % (self.id, self.room_id)


class TmpFileMap(db.Model):
    """
    临时文件的映射关系类
    """
    __tablename__ = "tmp_file_map"
    id = db.Column(db.String(100), primary_key=True)
    file_name = db.Column(db.String(150), nullable=False)
    file_format = db.Column(db.String(50), nullable=False)
    total_size = db.Column(db.Integer)
    current_size = db.Column(db.Integer)
    current_chunk = db.Column(db.Integer)
    room_id = db.Column(db.String(10))

    def __init__(self, file_identifer, file_name, total_size,
                 current_size, current_chunk, room_id):
        self.id = file_identifer
        self.file_name = file_name
        self.file_format = get_file_format(file_name)
        self.total_size = total_size
        self.current_size = current_size
        self.current_chunk = current_chunk
        self.room_id = room_id

    def __repr__(self):
        return 'File(id=%s, room_id=%s, current_size=%d)'\
            % (self.id, self.room_id, self.current_size)
