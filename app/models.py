#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-20

from . import login_manager
from app import db
from flask_login import UserMixin
import datetime


class Role(db.Document):
    name = db.StringField(maxlength=32, required=True, unique=True)
    annotation = db.StringField(maxlength=256)

    meta = {'collection': 'roles', 'strict': False}

    def __repr__(self):
        return "{id:%s, name:%s, read_permission:%s, write_permission:%s}" % (
            self.id, self.name, self.r_permission, self.w_permission)


class User(UserMixin, db.Document):
    email = db.EmailField(max_length=128, required=True, unique=True)
    password = db.StringField(max_length=128, required=True)
    name = db.StringField(max_length=32, required=True)
    role = db.ReferenceField(Role, required=True)
    register_time = db.DateTimeField(default=lambda: datetime.datetime.utcnow())
    last_login_time = db.DateTimeField(default=lambda: datetime.datetime.utcnow())
    # birthday = db.DateTimeField()
    # gender = StringField(max_length=8)
    # wx_id = StringField(max_length=64)

    meta = {'collection': 'users', 'strict': False}

    def __repr__(self):
        return "{id:%s, email:%s, name:%s, role:%s}" % (self.id, self.email, self.name, self.role)


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()
