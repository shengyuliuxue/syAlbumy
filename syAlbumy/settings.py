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








