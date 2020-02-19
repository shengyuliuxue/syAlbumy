#!usr/bin/env/python3
# -*- coding:utf-8 -*-

from flask import Flask, flash, request, redirect, url_for
from syAlbumy.register import register_bp
from syAlbumy.db import db
from syAlbumy.settings import SQLALCHEMY_DATABASE_URI
from flask_wtf import CSRFProtect
from syAlbumy.extensions import dropzone

UPLOAD_FOLDER = '/Users/shengyu/PycharmProjects/syAlbumy/syAlbumy/files'


def create_app():
    app = Flask(__name__)
    return app
csrf = CSRFProtect()
app = create_app()

app.register_blueprint(register_bp)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = '19870107'
app.config['DROPZONE_MAX_FILE_SIZE'] = 3
app.config['DROPZONE_MAX_FILES'] = 30
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image'
app.config['DROPZONE_ENABLE_CSRF'] = True

db.init_app(app)
csrf.init_app(app)
dropzone.init_app(app)

#with app.app_context():
#    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)