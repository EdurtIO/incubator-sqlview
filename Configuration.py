#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: Configuration.py 
@Time: 2020/12/29
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""

import os
import sys

import yaml
from flask import Flask
from flask_bootstrap import Bootstrap

from Logger import Logger
from utils.FileUtils import FileUtils

def get_root_path():
    """
    get project root path
    :return: root path
    """
    fileRoot = getattr(sys.modules['__main__'], '__file__')
    return os.path.abspath(os.path.dirname(fileRoot))

# load banner #
banner = os.path.join(get_root_path(), 'banner.txt')
Logger.info('load banner from %s', banner)
if FileUtils.exists(banner):
    file = open(file=banner)
    print(file.read())
    file.close()
else:
    Logger.info('banner not exists, skip it')

# load configuration #
Logger.info('start load default configuration file')
config = os.path.join(get_root_path(), 'configuration', 'sql-view.yaml')
Logger.info('load configuration from %s', config)
try:
    file = open(config, 'r')
    Configuration = yaml.load(file, Loader=yaml.FullLoader)
except Exception as ex:
    Logger.error('load configuration error %s', ex)
finally:
    FileUtils.close(file=file)
Logger.info('end load default configuration file')

# load flask #
Application = Flask(__name__)

# load bootstrap #
bootstrap = Bootstrap(Application)

