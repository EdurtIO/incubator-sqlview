#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: StringUtils.py 
@Time: 2020/12/29
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""

class StringUtils:

    @staticmethod
    def is_empty(message=None):
        """
        determines if the string is empty
        :param message: source string message
        :return: if null return true else false
        """
        return message is None or message == ''

    @staticmethod
    def is_not_empty(message=None):
        return not StringUtils.is_empty(message=message)
