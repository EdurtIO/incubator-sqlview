#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: __init__.py 
@Time: 2020/12/29
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from Configuration import Application, Logger
from views.view_editor import EditorView
from views.view_user import UserView

Logger.info('load views from view module')
Application.register_blueprint(UserView, url_prefix='/user')
Application.register_blueprint(EditorView, url_prefix='/editor')
