#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author: shicheng
@License: Apache Licence
@File: SqlViewApplication.py
@Time: 2020/12/29
@Contact: shicheng
@Site:
@Software: incubator-sqlview
"""

import time

from flask import render_template

from Configuration import Application
from Configuration import Configuration
from Configuration import Logger

@Application.errorhandler(404)
def page_not_found(message):
    print(message)
    return render_template('404.html', error=message)

@Application.route('/')
def index():
    return 'Hello SqlView'

if __name__ == '__main__':
    Logger.info('start server with %s', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    Logger.info('current system version <%s>', Configuration['server']['version'])
    Application.run(port=Configuration['server']['port'],
                    debug=Configuration['server']['debug'])
