# -*- coding: utf-8 -*-
"""Copy this file to config.py and fill needed field values"""
import os


class Config(object):
    DEBUG = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = '/tmp'
    TMP_UPLOAD_FOLDER = '/tmp'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'CAN YOU GUESS ME?'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    # Upload file
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    DEBUG = True

    # redis config
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
