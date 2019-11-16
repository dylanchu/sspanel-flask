#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-22

from flask import render_template, redirect, url_for, current_app, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from app import db
from app.models import User
from app.utils import is_local_url

from . import auth


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


@auth.route('/register', methods=['GET', 'POST'])
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
            return redirect(url_for('auth.dashboard'))
        else:
            flash('注册失败：用户以存在')
            return redirect(url_for('auth.login'))
    return render_template('register.html', form=form, url_register=url_for('auth.register'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        check_user = User.query.filter_by(email=form.email.data).first()
        if check_user:
            if check_user.password == current_app.md5_hash(form.password.data):
                login_user(check_user)
                if is_local_url(request.args.get('next')):
                    return redirect(request.args.get('next'))
                else:
                    return redirect(url_for('auth.dashboard'))
            flash('登录失败：用户名或密码不正确')
            return redirect(url_for('auth.login', next=request.args.get('next')))
        flash('登录失败：用户不存在')
        return redirect(url_for('auth.login', next=request.args.get('next')))
    return render_template('login.html', form=form, url_login=url_for('auth.login', next=request.args.get('next')))
    # return current_app.send_static_file('login.html')


@auth.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name, email=current_user.email)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.dashboard'))
