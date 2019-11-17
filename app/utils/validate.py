#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-28


from functools import wraps
from flask import jsonify
from flask_login import current_user, login_required

from app import errors


def admin_login_required(func):
    @login_required
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.level < 90:
            return jsonify(errors.Forbidden)
        return func(*args, **kwargs)
    return decorated_view


def is_local_url(url: str):
    if url.startswith('/'):
        return True
    return False
