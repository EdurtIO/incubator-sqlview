#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: TestStringUtils.py 
@Time: 2020/12/29
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""

from unittest import TestCase

from utils.utils_string import StringUtils

class TestStringUtils(TestCase):

    def test_isEmpty(self):
        message = 'i am not empty message'
        self.assertFalse(StringUtils.is_empty(message=message))
        message = ''
        self.assertTrue(StringUtils.is_empty(message=message))
