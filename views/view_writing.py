#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: view_writing.py 
@Time: 2021-01-07 16:33
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from flask import Blueprint, render_template
from flask_login import login_required

from common.common_method import Method

WritingView = Blueprint('WritingView', __name__, template_folder='templates')

@WritingView.route('/<type>', methods=[Method.GET.name])
@login_required
def index(type=None):
    if type == 'map':
        return render_template('writing/map.html')
