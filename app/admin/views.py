#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-28

from . import admin
from flask_login import login_required


@admin.route('/')
@login_required
def index():
    return 'admin homepage'
