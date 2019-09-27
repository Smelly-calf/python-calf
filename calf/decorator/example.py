#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
装饰器用法实例
1、身份认证
2、日志记录
"""
import functools
import time
from cachetools.func import lru_cache


def authenticate(func):
    """
    验证用户是否登录身份
    :param func: 函数
    :return: wrapper
    """

    def check_user_logged_in(request):
        print("check user logged_in:{}".format(request))

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request):
            return func(*args, **kwargs)
        else:
            raise Exception("Authentication failed")

    return wrapper


@lru_cache  # 缓存结果
def log_execution_time(func):
    """
    日志记录函数执行时间
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res

    return wrapper
