#!/usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@Author: shicheng 
@License: Apache Licence 
@File: coder_json.py 
@Time: 2021-01-07 11:08
@Contact: shicheng 
@Site:  
@Software: incubator-sqlview
"""
import json

from model.model_response import Response

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Response):
            return json.loads(json.dumps(o, default=lambda o: o.__dict__))
        return json.JSONEncoder.default(self, o)
