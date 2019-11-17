#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-28

from . import admin
from flask import jsonify, request, current_app
from app import db, errors
from app.models import User
from app.utils import admin_login_required


@admin.route('/')
@admin_login_required
def index():
    return jsonify(errors.success({
        'data': 'admin homepage'
    }))


@admin.route('/allUsers')
@admin_login_required
def get_all_users():
    users = User.query.all()
    return jsonify(errors.success({
        'data': list(map(User.to_dict, users))
    }))


@admin.route('/user', methods=['POST'])
@admin_login_required
def create_user():
    email = request.json.get('email')
    if email is not None:
        user = User.query.filter_by(id=email).first()
        if user:
            return jsonify(errors.User_already_exist)
        # todo: specify ss port ... before this is finished, the api will surely fail

        #     user = User(name='aaa', email='aaa@site.com', password='888888', ss_port='8081', ss_pwd='123456')
        #     try:
        #         db.session.add(user)
        #         db.session.commit()
        #     except Exception as e:
        #         return jsonify(errors.exception({
        #             'data': str(e)
        #         }))

        return jsonify(errors.success({
            'msg': '创建用户成功',
            'data': {
                'name': user.name,
                'email': user.email,
                'ss_port': user.ss_port
            }
        }))
    return jsonify(errors.Bad_request)


@admin.route('/user', methods=['DELETE'])
@admin_login_required
def delete_user():
    user_id = request.args.get('id')
    if user_id is not None:
        user = User.query.filter_by(id=user_id).first()
        if user:
            try:
                db.session.delete(user)
                db.session.commit()
            except Exception as e:
                return jsonify(errors.exception({
                    'data': str(e)
                }))
            return jsonify(errors.success({
                'msg': '删除用户完成',
                'data': {
                    'id': user.id,
                    'email': user.email
                }
            }))
        else:
            return jsonify(errors.User_not_exist)
    return jsonify(errors.Bad_request)


@admin.route('/user', methods=['PUT'])
@admin_login_required
def update_user():
    user_id = request.json.get('id')  # str
    if user_id is not None:
        user = User.query.filter_by(id=user_id).first()
        if user:
            for k, v in request.json.items():
                if k == 'password':
                    user.password = current_app.md5_hash(v)
                elif hasattr(user, k):
                    setattr(user, k, v)
            try:
                db.session.commit()
            except Exception as e:
                return jsonify(errors.exception({
                    'data': str(e)
                }))
            return jsonify(errors.success({
                'msg': '更新成功'
            }))
        else:
            return jsonify(errors.User_not_exist)
    return jsonify(errors.Bad_request)


@admin.route('/user', methods=['GET'])
@admin_login_required
def retrieve_user():
    user_id = request.args.get('id')
    if user_id is not None:
        user = User.query.filter_by(id=user_id).first()
        # user1 = User.query.filter(User.id == user_id).first() 亦可
        if user:
            return jsonify(errors.success(user.to_dict()))
        else:
            return jsonify(errors.User_not_exist)
    return jsonify(errors.Bad_request)
