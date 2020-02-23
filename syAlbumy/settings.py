#!usr/bin/env/python3
#-*- coding:utf-8 -*-
"""
    author:shengyu
    date:2020-02-11
"""

import os
import sys
import pprint

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

if sys.platform.startswith('win'):
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'



SQLALCHEMY_TRACK_MODIFICATIONS = False


SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'albumyData.db')

class BaseConfig:
    ALBUMY_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    ALBUMY_PHOTO_SIZE = {
        'small': 400,
        'medium': 800
    }

    ALBUMY_PHOTO_SUFFIX = {
        ALBUMY_PHOTO_SIZE['small']: '_s',
        ALBUMY_PHOTO_SIZE['medium']: '_m',
    }

    #UPLOAD_FOLDER = '/Users/shengyu/PycharmProjects/syAlbumy/syAlbumy/files'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SECRET_KEY = '19870107'
    DROPZONE_MAX_FILE_SIZE = 3
    DROPZONE_MAX_FILES = 30
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024
    DROPZONE_ALLOWED_FILE_TYPE = 'image'
    DROPZONE_ENABLE_CSRF = True




