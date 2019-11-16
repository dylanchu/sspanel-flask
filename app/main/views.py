#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-22

from . import main
from flask import current_app


@main.route('/')
@main.route('/index')
def index():
    return current_app.send_static_file('index.html')
