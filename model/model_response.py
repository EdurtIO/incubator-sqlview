#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: model_response.py 
@Time: 2021-01-07 10:53
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from common.common_code import Code

class Response:

    def __init__(self, status=Code.SUCCESS.name, message=None, result=None):
        self.status = status
        self.message = message
        self.result = result
