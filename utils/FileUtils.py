#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: FileUtils.py 
@Time: 2020/12/29
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
import os

from .StringUtils import StringUtils

class FileUtils:

    @staticmethod
    def exists(path=None):
        """
        determines if the path file is exists
        :param path: file path
        :return: if exists return true else false
        """
        if StringUtils.is_empty(path):
            return False
        else:
            return os.path.exists(path=path)

    @staticmethod
    def close(file=None):
        """
        close file stream
        :param file: file stream
        """
        if file is not None:
            file.close()
