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
from views.view_datasource import DataSourceView
from views.view_user import UserView
from views.view_writing import WritingView

Logger.info('load views from view module')
Application.register_blueprint(UserView, url_prefix='/user')
Application.register_blueprint(DataSourceView, url_prefix='/datasource')
Application.register_blueprint(WritingView, url_prefix='/writing')
