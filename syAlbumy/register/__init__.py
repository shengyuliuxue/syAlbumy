#usr/bin/env/python3
#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, abort,\
    request, redirect, flash, url_for, current_app, send_from_directory
from jinja2 import TemplateNotFound
from syAlbumy.register.forms import RegisterForm
from syAlbumy.model import User
from syAlbumy.db import db
from werkzeug.utils import secure_filename
import os
from flask_dropzone import random_filename
from flask_sqlalchemy import Pagination

register_bp = Blueprint('register_bp', __name__, template_folder='templates')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}
from syAlbumy.model import Photo
from syAlbumy.utils import resize_image

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


def allowed_file(filename):
    return '.' in filename and \
                    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#test update file
@register_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    # check if the post request has the file part
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        #if user doed not select file, browser also
        #submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['ALBUMY_UPLOAD_PATH'], filename))
            return redirect(url_for('register_bp.upload'))

    return render_template('update.html')

@register_bp.route('/upphoto', methods=['GET','POST'])
def upphoto():
    if request.method == 'POST' and 'file' in request.files:
        f = request.files.get('file')
        filename = random_filename(f.filename)
        path = os.path.join(current_app.config['ALBUMY_UPLOAD_PATH'], filename)
        f.save(path)
        filename_s = resize_image(filename, path, 400)
        filename_m = resize_image(filename, path, 800)

        photo = Photo(
            filename=filename,
            filename_s=filename_s,
            filename_m=filename_m,
            user_id=1
        )

        db.session.add(photo)
        db.session.commit()
    return render_template('update.html')


@register_bp.route('/upphoto/<path:filename>')
def get_image(filename):
    return send_from_directory(current_app.config['ALBUMY_UPLOAD_PATH'], filename)

@register_bp.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    per_page = 9
    pagination = Photo.query.filter_by(user_id=user.id).paginate(page, per_page)
    photos = pagination.items
    return render_template('user/_header.html', user=user, photos=photos)


@register_bp.route('/profile/<user_id>')
def get_profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user/profile.html', user=user)

