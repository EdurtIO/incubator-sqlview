#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: Logger.py 
@Time: 2020/12/29
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""

import logging as Logger

FORMAT = '%(asctime)-15s - %(name)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s'
Logger.basicConfig(format=FORMAT, level=Logger.DEBUG)
Logger.getLogger('SqlView')
