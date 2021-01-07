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

class UserModel(UserMixin):

    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password
        self.authenticated = False

    def is_active(self):
        return self.is_active()

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def verify_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')
