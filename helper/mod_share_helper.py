# -*- coding: utf-8 -*-
import random
from app.mod_share.models import File


def get_file_format(filename):
    """
    根据文件名获取文件格式
    """
    if '.' in filename:
        return filename.rsplit('.', 1)[1]
    else:
        return "unknown"


def generate_random_hash():
    """
    生成一个随机的哈希码
    """
    hash = random.getrandbits(128)
    return "%032x" % hash


def generate_file_id():
    """
    生成随机8位数字用作文件的id，且是数据库中已存在id
    """
    file_id = random.randint(10000000, 99999999)
    while File.query.get(file_id) != None:
        file_id = random.randint(10000000, 99999999)
    return file_id
