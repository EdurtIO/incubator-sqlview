#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: service_user.py 
@Time: 2020-12-30 22:31
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from connect.connect_sqlite3 import ConnectSqlite
from model.model_user import UserModel

class ServiceUser:

    def save(model=UserModel):
        connection = ConnectSqlite.connect()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO user(username, password) values(?,?)', (model.username, model.password))
        connection.commit()
        cursor.close()
