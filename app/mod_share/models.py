# -*- coding: utf-8 -*-
from app import db


class File(db.Model):
    __tablename__ = 'share_file'
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(150), nullable=False)
    file_format = db.Column(db.String(50), nullable=False)
    hash_code = db.Column(db.String(128), unique=True)

    def __init__(self, file_id, file_name, file_format, hash_code):
        self.id = file_id
        self.file_name = file_name
        self.file_format = file_format
        self.hash_code = hash_code

    def __repr__(self):
        return 'File(id=%d, hash_code=%s)'\
            % (self.id, self.hash_code)
