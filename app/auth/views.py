#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-22

from flask import current_app, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from app import db, errors
from app.models import User

from . import auth


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


@auth.route('/register', methods=['POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User()
            user.email = form.email.data
            user.password = current_app.md5_hash(form.password.data)
            user.name = form.name.data
            # todo: allocate ss_port and ss_pwd for new user!
            db.session.add(user)  # before above todo is solved, this will surely fail
            db.session.commit()
            login_user(user)
            return jsonify(errors.success({
                'name': user.name,
                'email': user.email
            }))
        else:
            return jsonify(errors.User_already_exist)
    return jsonify(errors.Bad_request)


@auth.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return jsonify(errors.Already_logged_in)
    form = LoginForm()
    if form.validate_on_submit():
        check_user = User.query.filter_by(email=form.email.data).first()
        if check_user:
            if check_user.password == current_app.md5_hash(form.password.data):
                login_user(check_user)
                return jsonify(errors.success({
                    'name': check_user.name,
                    'email': check_user.email
                }))
            return jsonify(errors.Authorize_failed)
        return jsonify(errors.User_not_exist)


@auth.route('/whoami')
@login_required
def whoami():
    return jsonify(errors.success({
        'data': {
            'name': current_user.name,
            'email': current_user.email
        }
    }))


@auth.route('/logout', methods=['POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
    return jsonify(errors.success())
