#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: view_common.py 
@Time: 2020-12-30 00:49
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from flask import Blueprint, render_template

CommonView = Blueprint('CommonView', __name__, template_folder='templates')

@CommonView.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
