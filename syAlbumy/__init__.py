#!usr/bin/env/python3
# -*- coding:utf-8 -*-

from flask import Flask
from syAlbumy.register import register_bp
from syAlbumy.db import db
from syAlbumy.settings import SQLALCHEMY_DATABASE_URI

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

app.register_blueprint(register_bp)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

#with app.app_context():
#    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)