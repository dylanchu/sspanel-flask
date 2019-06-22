#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-15

import hashlib


class BaseConfig(object):
    LOG_LEVEL = 'DEBUG'  # DEBUG, INFO, WARNING, ERROR, CRITICAL. 可使用app.logger.exception(msg)，但level没有EXCEPTION
    SECRET_KEY = 'dL28o(19xi54h2?3BX90k92R'  # 为安全推荐从环境变量获取

    # session
    SESSION_TYPE = 'filesystem'  # filesystem(采用flask默认的保存在cookie中),可为redis/memcached等
    # SESSION_TYPE为null时会导致exception
    # https://stackoverflow.com/questions/26080872/secret-key-not-set-in-flask-session-using-the-flask-session-extension
    SESSION_USE_SIGNER = True  # 是否强制加盐混淆session
    SESSION_PERMANENT = True  # 是否长期有效，false则关闭浏览器失效
    PERMANENT_SESSION_LIFETIME = 7200  # 重要,session有效期(秒),默认永久有效

    # mongoengine, https://flask-mongoengine.readthedocs.io/en/latest/
    MONGODB_SETTINGS = {
        'db': 'expression_flask',
        'host': '127.0.0.1',
        'port': 27017,
        # if authentication is needed:
        # 'username': 'webapp',
        # 'password': 'pwd123',
        'connect': False  # False: connect when first connect instead of instantiated
    }

    # 自定义
    @staticmethod
    def MD5_HASH(password) -> str:
        _MD5_SALT = 'a random string'
        _MD5_TOOL = hashlib.md5()
        _MD5_TOOL.update((password + _MD5_SALT).encode())
        return _MD5_TOOL.hexdigest()


class DevelopmentConfig(BaseConfig):
    import os
    SECRET_KEY = os.urandom(24)  # 设为24位的随机字符,重启服务器则上次session清除
    WTF_CSRF_ENABLED = False  # 是否开启flask-wtf的csrf保护,默认是True,用postman提交表单测试需要设为False

    SESSION_USE_SIGNER = False
    # from redis import Redis
    # SESSION_TYPE = 'redis'  # null(采用flask默认的保存在cookie中) / redis / memcached / ..
    # SESSION_REDIS = Redis(host='127.0.0.1', port=6379, db=0, password=None)
    # SESSION_KEY_PREFIX = 'flask_session:'  # session的redis等键名前缀,默认为'session:'

    # SQLALCHEMY_DATABASE_URI = 'mysql://username:password@hostname/database'
    # SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/test'
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']


class SsConfig(object):
    SS_DEFAULT_TRAFFIC = 100  # 单位：MB
