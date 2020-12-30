#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: connect_redis.py 
@Time: 2020-12-30 12:46
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
import redis

from Configuration import Logger

class ConnectRedis:

    @staticmethod
    def connect(host='localhost', port=6379, maxConnections=1000, dbIndex=0):
        Logger.info('init redis connection pool from %s port %s database %s', host, port, dbIndex)
        Pool = redis.ConnectionPool(host=host, port=port, max_connections=maxConnections, db=dbIndex,
                                    decode_responses=True)
        RedisClient = redis.Redis(connection_pool=Pool)
        return RedisClient
