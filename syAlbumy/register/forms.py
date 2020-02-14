#usr/bin/env/python3
#-*- coding:utf-8 -*-

from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from syAlbumy.model import User

class RegisterForm(Form):
    name = StringField('name', validators=[DataRequired(), Length(1, 30)])
    email = StringField('email', validators=[DataRequired(),Email(), Length(1, 64)])
    username = StringField('username', validators=[DataRequired(), Length(1, 20),
                                                   Regexp('^[0-9a-zA-Z\_]*$')])
    password = PasswordField('password', validators=[DataRequired(), Length(1, 20)])
    confirmpassword = PasswordField('confirmpassword', validators=[DataRequired(), EqualTo('password',
                                                                                           message='Passwords must match')])
    submit = SubmitField('submit')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data.lower()).first():
            raise ValidationError('The username is in use!')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('The email is in use!')


