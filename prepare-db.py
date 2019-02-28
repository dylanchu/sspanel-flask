#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-25

from app.models import Role, User
from run_app import app

admin_role = Role()
admin_role.name = 'admin'
admin_role.save()

default_role = Role()
default_role.name = 'default'
default_role.save()

admin = User()
admin.email = 'admin@site.com'
admin.password = app.md5_hash('1234')
admin.name = '管理员1'
admin.role = admin_role
admin.save()

user1 = User()
user1.email = 'aaa@site.com'
user1.password = app.md5_hash('1234')
user1.name = '张三'
user1.role = default_role
user1.save()

user2 = User()
user2.email = 'bbb@site.com'
user2.password = app.md5_hash('1234')
user2.name = '李四'
user2.role = default_role
user2.save()
