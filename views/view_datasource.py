#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: view_editor.py 
@Time: 2020-12-30 12:27
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from flask import Blueprint, render_template
from common.common_method import Method

DataSourceView = Blueprint('DataSourceView', __name__, template_folder='templates')

@DataSourceView.route('/', methods=[Method.GET.name, Method.POST.name])
# @login_required
def index():
    return render_template('editor/common.html')
