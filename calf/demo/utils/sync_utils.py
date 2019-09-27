#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
序列化 和 反序列化 config.json
"""
import json


def serialize(obj, output):
    with open(output, 'w') as config:
        try:
            json.dump(obj, config)
        except Exception as e:
            print(e)


def unserialize(str):
    return json.loads(str)