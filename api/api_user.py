#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: api_user.py 
@Time: 2021-01-07 10:13
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from flask import Blueprint, jsonify

from common.common_code import Code
from common.common_method import Method
from model.model_response import Response
from model.model_user import UserModel
from service.service_user import UserService
from utils.utils_request import RequestUtils
from utils.utils_string import StringUtils
from werkzeug.security import generate_password_hash
from flask import request

UserApi = Blueprint('UserApi', __name__, template_folder='templates')

@UserApi.route('register', methods=[Method.POST.name])
def register():
    response = Response()
    username = RequestUtils.get_value(key='username')
    password = RequestUtils.get_value(key='password')
    re_password = RequestUtils.get_value(key='re-password')
    if StringUtils.is_empty(username) or StringUtils.is_empty(password) or StringUtils.is_empty(re_password):
        response.status = Code.FAILURE.name
        response.message = 'Input parameter must not null. Please check it!'
        return jsonify(response)
    if password != re_password:
        response.status = Code.FAILURE.name
        response.message = 'The two passwords are inconsistent. Please check it!'
        return jsonify(response)
    user = UserService.find_username(username=username)
    if user is not None:
        response.status = Code.FAILURE.name
        response.message = 'The registered user already exists, please change another username!'
        return jsonify(response)
    user = UserModel(username=username, password=password)
    UserService.save(model=user)
    response.status = Code.SUCCESS.name
    return jsonify(response)
