#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-28


def is_local_url(url: str):
    if url.startswith('/'):
        return True
    return False
