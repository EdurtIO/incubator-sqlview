#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: utils_request.py 
@Time: 2021-01-07 11:43
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""

from flask import request

from Configuration import Logger
from utils.utils_string import StringUtils

class RequestUtils:

    @staticmethod
    def get_value(key=None):
        result = None
        if StringUtils.is_not_empty(key):
            try:
                jsonResponse = request.get_json()
                result = jsonResponse[key]
            except Exception as ex:
                Logger.error('get data from json error %s', ex)
        return result
