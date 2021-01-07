#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: __init__.py 
@Time: 2020-12-30 17:53
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from api.api_redis import RedisApi
from api.api_user import UserApi
from Configuration import Application

Application.register_blueprint(RedisApi, url_prefix='/api/v1/redis')
Application.register_blueprint(UserApi, url_prefix='/api/v1/user')
