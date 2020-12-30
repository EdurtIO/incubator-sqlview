#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: model_user.py 
@Time: 2020-12-30 01:09
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

USERS = [
    {
        "id": 1,
        "name": 'demo1',
        "password": generate_password_hash('123')
    },
    {
        "id": 2,
        "name": 'demo2',
        "password": generate_password_hash('123')
    }
]

class UserModel(UserMixin):

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def verify_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    def get_id(self):
        return self.id

    @staticmethod
    def get(user_id):
        if not user_id:
            return None
        for user in USERS:
            if user.get('id') == user_id:
                return UserModel(user)
        return None
