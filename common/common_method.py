#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: CommonMethod.py
@Time: 2020-12-30 10:43
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from enum import Enum, unique

@unique
class Method(Enum):
    POST = 'POST'
    GET = 'GET'
    DELETE = 'DELETE'
    PUT = 'PUT'
