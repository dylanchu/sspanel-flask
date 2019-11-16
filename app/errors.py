#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-11-17


# 应前段要求把x改在data里面
def success(x=None):
    """
    :type x: dict or None
    :return: dict
    """
    d = {'code': 0, 'msg': 'success', 'data': {}}
    if x:
        for t in x:
            if t == 'code' or t == 'msg':
                d[t] = x[t]
            else:
                d['data'][t] = x[t]
    return d


def info(msg, x=None):
    d = {'code': 2, 'msg': msg, 'data': {}}
    if x:
        for t in x:
            if t == 'code' or t == 'msg':
                d[t] = x[t]
            else:
                d['data'][t] = x[t]
    return d


def error(x=None):
    """
    :type x: dict or None
    :return: dict
    """
    d = {'code': 1, 'msg': 'error', 'data': {}}
    if x:
        for t in x:
            if t == 'code' or t == 'msg':
                d[t] = x[t]
            else:
                d['data'][t] = x[t]
    return d


def exception(x=None):
    """
    :type x: dict or None
    :return: dict
    """
    d = {'code': 1, 'msg': 'exception', 'data': {}}
    if x:
        for t in x:
            if t == 'code' or t == 'msg':
                d[t] = x[t]
            else:
                d['data'][t] = x[t]
    return d


def redirect(next_url):
    """
    :type next_url: str
    :return: dict
    """
    d = {'code': 3, 'msg': 'redirect'}
    if next_url:
        return {**d, **{'data': {'redirect': next_url}}}
    return d


Params_error = {'code': 4000, 'msg': '请求参数错误'}

Authorize_needed = {'code': 4300, 'msg': '需要登录'}
Authorize_failed = {'code': 4301, 'msg': '账号或密码错误'}
User_not_exist = {'code': 4302, 'msg': '用户不存在'}
User_already_exist = {'code': 4303, 'msg': '用户已存在'}
Already_logged_in = {'code': 4304, 'msg': '用户已经登录'}
Register_not_allowed = {'code': 4305, 'msg': '当前不允许注册'}
Unauthorized = {'code': 4306, 'msg': '未授权'}
Illegal_invitation_code = {'code': 4039, 'msg': '无效的邀请码'}
Wechat_already_bind = {'code': 4040, 'msg': '该账号已绑定微信，若需重新绑定，请先解绑原微信号'}
Wechat_not_bind = {'code': 4041, 'msg': '未绑定微信，不需要解绑'}

WIP = {'code': 5104, 'msg': '正在处理'}
