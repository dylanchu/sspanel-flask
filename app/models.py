#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-20

from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from config import SsConfig


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'useexisting': True}
    note = db.Column(db.String(256), nullable=True, default=None)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    level = db.Column(db.SmallInteger, nullable=False, default=0)
    email = db.Column(db.String(32), unique=True, nullable=False)  # probably temp email if address too long
    password = db.Column(db.String(48), name='password', nullable=False)
    ss_port = db.Column(db.Integer, nullable=False, unique=True)
    ss_pwd = db.Column(db.String(16), name='ss_pwd', nullable=False)

    ss_enabled = db.Column(db.Boolean, nullable=False, default=True)  # boolean will convert to tinyint(1) in mysql?
    ss_method = db.Column(db.String(32), nullable=False, default='aes-128-cfb')
    traffic_up = db.Column(db.BigInteger, nullable=False, default=0)
    traffic_down = db.Column(db.BigInteger, nullable=False, default=0)
    traffic_quota = db.Column(db.BigInteger, nullable=False,
                              default=SsConfig.SS_DEFAULT_TRAFFIC * 1024 * 1024)
    last_use_time = db.Column(db.DateTime, nullable=False, default=datetime.fromisoformat('1999-01-01 08:00:00'))
    plan_type = db.Column(db.String(32), nullable=False, default='free')
    plan_end_time = db.Column(db.DateTime, nullable=False, default=datetime.fromisoformat('2099-12-31 12:00:00'))
    total_paid = db.Column(db.Integer, nullable=False, default=0)
    last_gift_time = db.Column(db.DateTime, nullable=False, default=datetime.fromisoformat('1999-01-01 08:00:00'))
    last_check_in_time = db.Column(db.DateTime, nullable=False, default=datetime.fromisoformat('1999-01-01 08:00:00'))
    last_reset_pwd_time = db.Column(db.DateTime, nullable=False, default=datetime.fromisoformat('1999-01-01 08:00:00'))
    reg_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow())
    reg_ip = db.Column(db.CHAR(39), nullable=False, default='127.0.0.1')
    referee = db.Column(db.Integer, nullable=False, default=0)
    invite_quota = db.Column(db.SmallInteger, name='invite_num', nullable=False, default=0)
    email_verified = db.Column(db.Boolean, nullable=False, default=False)
    protocol = db.Column(db.CHAR(32), nullable=False, default='origin')
    obfs = db.Column(db.CHAR(32), nullable=False, default='plain')
    type = db.Column(db.SmallInteger, nullable=False, default=1)

    def __init__(self, **kwargs):
        for k in kwargs:
            if hasattr(self, k):
                self.__dict__[k] = kwargs[k]

    def __repr__(self):
        return "{id:%s, email:%s, name:%s}" % (self.id, self.email, self.name)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
