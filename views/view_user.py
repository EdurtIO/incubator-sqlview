#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: view_user.py 
@Time: 2020-12-30 00:36
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from flask import Blueprint, render_template
from Configuration import LoginManagerFactory

from model.model_user import UserModel

UserView = Blueprint('UserView', __name__, template_folder='templates', static_folder='static')

@LoginManagerFactory.user_loader
def load_user(user_id):
    return UserModel.get(user_id=user_id)

@UserView.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('user/login.html', title='User Login')
