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
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user as CurrentUser, login_user, logout_user

from common.CommonMethod import Method
from Configuration import LoginManagerFactory
from model.model_user import UserModel
from service.service_user import ServiceUser

UserView = Blueprint('UserView', __name__, template_folder='templates', static_folder='static')

@LoginManagerFactory.user_loader
def load_user(user_id):
    return UserModel.get(user_id=user_id)

@UserView.route('/login', methods=[Method.GET.name, Method.POST.name])
def login():
    if CurrentUser.is_authenticated:
        print('current user is login success!')
    if request.method == Method.POST.name:
        login_user(UserModel.get(1))
        return redirect(url_for('CommonView.index'))
    return render_template('user/login.html', title='User Login')

@UserView.route('register', methods=[Method.GET.name, Method.POST.name])
def register():
    if request.method == Method.POST.name:
        username = request.form.get('username')
        password = request.form.get('password')
        print(request.form)
        model = UserModel(username=username, password=password)
        print(model.username)
        ServiceUser.save(model=model)
        return None
    return render_template('user/register.html', title='User Register')

@UserView.route('/logout')
def logout():
    logout_user()
    flash(u'The current user has logged out!')
    return redirect(url_for('UserView.login'))

@LoginManagerFactory.unauthorized_handler
def unauthorized():
    flash('You do not have access to the current page, please log in.')
    return redirect(url_for('UserView.login'))
