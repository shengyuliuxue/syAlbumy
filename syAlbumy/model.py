#!usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
    author:shengyu
    date:2020-02-10 at home
    @copyright reserved.
"""

from syAlbumy.db import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

collections_table = db.Table('collections', db.Column('user_id', db.Integer, db.ForeignKey('user.id'),),
                             db.Column('photo_id', db.Integer, db.ForeignKey('photo.id')))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(30),  nullable=False)
    password_hash = db.Column(db.String(120))

    def setPassword(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        check_password_hash(self.password_hash, password)

    comments = db.relationship('Comment', back_populates='user')
    photos = db.relationship('Photo', secondary=collections_table, back_populates='users')


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    #resource
    photo_comment = db.relationship('Comment', back_populates='photo')
    users = db.relationship('User', secondary=collections_table, back_populates='photos')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    context = db.Column(db.Text, nullable=False)
    time = db.Column(db.Time, default=datetime.utcnow)
    photo_id = db.Column(db.Integer, db.ForeignKey('photo.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='comments')
    photo = db.relationship('Photo', back_populates='photo_comment')






