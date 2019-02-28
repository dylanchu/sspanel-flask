#!/usr/bin/env python3
# coding: utf-8
#
# Created by dylanchu on 19-2-22

from app import create_app

app = create_app()

if __name__ == '__main__':
    # handler = logging.FileHandler('flask.log')
    # app.logger.addHandler(handler)
    app.run()
