# -*- coding: utf-8 -*-
from app import db


class Manager(db.Model):
    """
    房间管理员的存储类
    """
    __tablename__ = 'chat_room'
    id = db.Column(db.Integer, primary_key=True)
    manager_email = db.Column(db.String(150), nullable=False)
    manager_password = db.Column(db.String(150), nullable=False)
    manager_name = db.Column(db.String(150), nullable=False)

    def __init__(self, manager_email, manager_password, manager_name):
        self.manager_email = manager_email
        self.manager_password = manager_password
        self.manager_name = manager_name

    def __repr__(self):
        return 'Manager(id=%d, manager_name=%s)'\
            % (self.id, self.manager_name)
