# -*- coding: utf-8 -*-
from app import db


class Manager(db.Model):
    """
    房间管理员的存储类
    """
    __tablename__ = 'manager'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)

    def __init__(self, manager_email, manager_password, manager_name):
        self.email = manager_email
        self.password = manager_password
        self.name = manager_name

    def __repr__(self):
        return 'Manager(id=%d, email=%s)'\
            % (self.id, self.email)
