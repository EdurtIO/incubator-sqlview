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

EditorView = Blueprint('EditorView', __name__, template_folder='templates')

@EditorView.route('/', methods=['GET', 'POST'])
# @login_required
def index():
    return render_template('editor/common.html')
