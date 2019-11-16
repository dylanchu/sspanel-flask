#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-28

from . import admin
from flask import jsonify
from flask_login import login_required
from app import db, errors
from app.models import User
from app.utils import admin_required


@admin.route('/')
@login_required
@admin_required
def index():
    return jsonify(errors.success({
        'data': 'admin homepage'
    }))


@admin.route('/db_test/c')
@login_required
@admin_required
def db_test_create():
    user = User(name='aaa', email='aaa@site.com', password='888888', ss_port='8081', ss_pwd='123456')
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        return jsonify(errors.exception({
            'data': str(e)
        }))
    return jsonify(errors.success({
        'name': user.name,
        'email': user.email,
        'ss_port': user.ss_port
    }))


@admin.route('/db_test/r')
@login_required
@admin_required
def db_test_retrieve_using_email():  # 检索
    user1 = User.query.filter_by(email='aaa@site.com').first()
    # user1 = User.query.filter(User.email == 'aaa@site.com').first()  也可以
    if user1:
        return jsonify(errors.success({
            'name': user1.name,
            'email': user1.email,
            'ss_port': user1.ss_port
        }))
    else:
        return jsonify(errors.User_not_exist)


@admin.route('/db_test/u')
@login_required
@admin_required
def db_test_update_using_email():
    user1 = User.query.filter_by(email='aaa@site.com').first()
    if user1:
        user1.name = 'A New Name'
        db.session.commit()
    else:
        return jsonify(errors.User_not_exist)
    return db_test_retrieve_using_email()


@admin.route('/db_test/delete')
@login_required
@admin_required
def db_test_delete_using_email():
    user1 = User.query.filter_by(email='aaa@site.com').first()
    if user1:
        db.session.delete(user1)
        db.session.commit()
    return jsonify(errors.success({
        'data': '删除成功，请再次查询验证'
    }))
