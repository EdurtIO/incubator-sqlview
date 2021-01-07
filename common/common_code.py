#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: common_code.py 
@Time: 2021-01-07 10:57
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
from enum import Enum, unique

@unique
class Code(Enum):
    SUCCESS = 2000,
    FAILURE = 4000
