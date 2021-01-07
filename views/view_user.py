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
from passlib.hash import sha256_crypt

from common.common_method import Method
from Configuration import LoginManagerFactory
from model.model_user import UserModel
from service.service_user import UserService

UserView = Blueprint('UserView', __name__, template_folder='templates', static_folder='static')

@LoginManagerFactory.user_loader
def load_user(id=None):
    if not id:
        return None
    user = UserService.find_id(id=id)
    if user is None:
        return None
    else:
        return UserModel(int(user[0]), user[1], user[2])

@UserView.route('/login', methods=[Method.GET.name, Method.POST.name])
def login():
    if CurrentUser.is_authenticated:
        flash('current user is login success!')
        return redirect(url_for('CommonView.index'))
    if request.method == Method.POST.name:
        username = request.form.get('username')
        password = request.form.get('password')
        user = UserService.find_username(username=username)
        if user is None:
            flash('Invalid username')
            return redirect(url_for('UserView.login'))
        if not sha256_crypt.verify(password, user[2]):
            flash('Invalid password')
            return redirect(url_for('UserView.login'))
        user_session = load_user(user[0])
        login_user(user_session)
        return redirect(url_for('CommonView.index'))
    return render_template('user/login.html', title='User Login')

@UserView.route('register', methods=[Method.GET.name])
def register():
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
