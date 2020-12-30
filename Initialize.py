#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: Initialize.py 
@Time: 2020-12-30 22:39
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from Configuration import Configuration
from connect.connect_sqlite3 import ConnectSqlite

if __name__ == '__main__':
    print('#### initialize db ####')
    cursor = ConnectSqlite.connect().cursor();
    cursor.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY, username VARCHAR , password VARCHAR)')
