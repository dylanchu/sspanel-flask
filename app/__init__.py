#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-22

from app import errors
from config import DevelopmentConfig
from flask import Flask, jsonify
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'  # 访问需要已登录才能访问的地址时，调用的 登录页面函数
login_manager.unauthorized = lambda: jsonify(errors.Authorize_needed)  # 重写需要登录的处理函数


def create_app():
    app = Flask(__name__, static_url_path='/static')  # 要映射静态文件到根目录下用static_url_path=''

    app.config.from_object(DevelopmentConfig)
    app.logger.setLevel(app.config['LOG_LEVEL'])

    Session(app)
    db.init_app(app)
    login_manager.init_app(app)

    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint, static_folder='static')
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/api/admin')

    app.md5_hash = app.config['MD5_HASH']

    return app
