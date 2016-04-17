# -*- coding: utf-8 -*-
"""
该文件用于定义一些通用的函数
"""
import random


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


def generate_random_num_str(n):
    """
    生成n位随机数字字符串
    """
    result_num = ""
    for i in range(n):
        result_num += str(random.randint(0, 9))
    return result_num
