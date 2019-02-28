#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-25

from flask import Blueprint

api = Blueprint('api', __name__)

from . import views
