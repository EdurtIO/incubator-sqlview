#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: connect_sqlite3.py 
@Time: 2020-12-30 21:56
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
import sqlite3

from Configuration import Logger, Configuration

class ConnectSqlite:

    @staticmethod
    def connect():
        Logger.info('init sqlite connection from %s', Configuration['db']['path'])
        SqliteClient = sqlite3.connect(Configuration['db']['path'])
        return SqliteClient
