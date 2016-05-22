# -*- coding: utf-8 -*-
import datetime
from . import db
from models.manage_mod import Manager
from models.chat_mod import Room
db.session.add(
    Manager(
        manager_email="123456@qq.com",
        manager_password="123456",
        manager_name=u"御坂美琴"
    )
)

db.session.add(
    Room(
        room_id='123456',
        room_name=u'御坂美琴の粉丝团1',
        start_time=1463939795682,
        end_time=1463939797682,
        description=u'御坂美琴',
        manager_id=1
    )
)

db.session.add(
    Room(
        room_id='123457',
        room_name=u'御坂美琴の粉丝团2',
        start_time=1463939795682,
        end_time=1463939895682,
        description=u'御坂美琴',
        manager_id=1
    )
)
db.session.commit()
