# -*- coding: utf-8 -*-
from app import db
from app.common import get_file_format


class File(db.Model):
    """
    文件的存储类
    """
    __tablename__ = 'share_file'
    id = db.Column(db.String(128), primary_key=True)
    file_name = db.Column(db.String(150), nullable=False)
    file_format = db.Column(db.String(50), nullable=False)
    group_code = db.Column(db.String(128))

    def __init__(self, file_id, file_name, file_format, group_code):
        self.id = file_id
        self.file_name = file_name
        self.file_format = file_format
        self.group_code = group_code

    def __repr__(self):
        return 'File(id=%s, group_code=%s)'\
            % (self.id, self.group_code)


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
    group_code = db.Column(db.Integer)

    def __init__(self, file_identifer, file_name, total_size,
                 current_size, current_chunk, group_code):
        self.id = file_identifer
        self.file_name = file_name
        self.file_format = get_file_format(file_name)
        self.total_size = total_size
        self.current_size = current_size
        self.current_chunk = current_chunk
        self.group_code = group_code

    def __repr__(self):
        return 'File(id=%s, group_code=%s, current_size=%d)'\
            % (self.id, self.group_code, self.current_size)
