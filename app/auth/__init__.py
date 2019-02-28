#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-23

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
