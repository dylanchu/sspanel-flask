#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-28

from . import admin
from flask_login import login_required
from app import db
from app.models import User


@admin.route('/')
@login_required
def index():
    return 'admin homepage'


@admin.route('/db_test/c')
def db_test_create():
    user = User(name='aaa', email='aaa@site.com', password='888888', ss_port='8081', ss_pwd='123456')
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        return str(e)
    return 'ok' + str(user.__dict__)


@admin.route('/db_test/r')
def db_test_retrieve():
    user1 = User.query.filter_by(email='aaa@site.com').first()
    # user1 = User.query.filter(User.email == 'aaa@site.com').first()  也可以
    if user1:
        return str(user1.__dict__)
    else:
        return 'not found'


@admin.route('/db_test/u')
def db_test_update():
    user1 = User.query.filter_by(email='aaa@site.com').first()
    user1.name = 'A New Name'
    db.session.commit()
    return db_test_retrieve()


@admin.route('/db_test/delete')
def db_test_delete():
    user1 = User.query.filter_by(email='aaa@site.com').first()
    if user1:
        db.session.delete(user1)
    db.session.commit()
    return 'ok<br>query again:' + db_test_retrieve()
