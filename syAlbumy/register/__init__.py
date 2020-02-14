#usr/bin/env/python3
#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, abort, request, redirect
from jinja2 import TemplateNotFound
from syAlbumy.register.forms import RegisterForm
from syAlbumy.model import User
from syAlbumy.db import db

register_bp = Blueprint('register_bp', __name__, template_folder='templates')

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data.lower()
        username = form.username.data
        password = form.password.data
        user = User(name=name, email=email, username=username)
        user.setPassword(password)
        db.session.add(user)
        db.session.commit()
        return redirect("https://www.baidu.com")
    return render_template('register/register.html', form=form)
