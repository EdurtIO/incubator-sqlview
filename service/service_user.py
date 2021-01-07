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
from werkzeug.security import generate_password_hash

from connect.connect_sqlite3 import ConnectSqlite
from model.model_user import UserModel

class UserService:

    def save(model=UserModel):
        connection = ConnectSqlite.connect()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO user(username, password) values(?,?)',
                       (model.username, generate_password_hash(model.password, method='sha256')))
        connection.commit()
        cursor.close()

    def find_username(username=None):
        connection = ConnectSqlite.connect()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
        row = cursor.fetchone()
        return row

    def find_username_password(username=None, password=None):
        connection = ConnectSqlite.connect()
        cursor = connection.cursor()
        rows = cursor.execute('SELECT * FROM user WHERE username = ? AND password = ?',
                              (username, generate_password_hash(password, method='sha256')))
        for row in rows:
            print(row)
