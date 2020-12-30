#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: api_redis.py 
@Time: 2020-12-30 17:46
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from flask import Blueprint, jsonify, request

from common.CommonMethod import Method
from connect.connect_redis import ConnectRedis

RedisApi = Blueprint('RedisApi', __name__, template_folder='templates')

@RedisApi.route('', methods=[Method.GET.name])
# @login_required
def get():
    array = []
    type = request.args.get('type')
    index = request.args.get('index')
    # RedisClient = ConnectRedis.connect(dbIndex=index)
    if type == 'database':
        count = 12 # RedisClient.config_get('databases')['databases']
        for index in range(int(count)):
            array.append({
                'text': 'db' + str(index),
                'icon': 'fa fa-database',
                'type': 'database'
            })
    elif type == 'table':
        keys = ['12', '13']#RedisClient.keys()
        for key in keys:
            array.append({
                'text': key,
                'icon': 'fa fa-table',
                'type': 'table'
            })
    return jsonify(array)
