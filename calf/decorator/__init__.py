#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
函数->装饰器

必须掌握的函数的几个核心概念：
1、一等公民(first-class citizen)；也是对象，可以把函数赋给变量。
2、函数可以作为参数传入另一个函数
3、函数中定义函数。
4、函数的返回值也可以是函数对象(闭包)


@语法糖
带有参数的装饰器，实际调用的是装饰器中的 wrapper 函数
*args, **kwargs 兼容所有函数
@functools.wraps(func)：保留原函数信息
"""
import functools
import inspect


def mydecorator(func):
    def wrapper(*args):
        print("wrapper of decorator.")
        func(*args)

    return wrapper


def greet(name):
    print("Hello ,{}".format(name))


# mydecorator 是一个装饰器，把 greet 函数包裹在其中。
# greet = mydecorator(greet)
# greet(1)


# 使用语法糖使表达更简洁
@mydecorator
def greet():
    print("Hello world.")


# greet()
# 打印函数信息:'wrapper'
# print(greet.__name__)

cache_data_map = {}


class MemCache():

    def cache(self, namespace=None, key_func=None):

        def wrapper(f):
            print("wrapper")
            argspec = inspect.getargspec(f)
            has_self = bool(argspec[0]) and argspec[0][0] in ('self', 'cls')

            @functools.wraps(f)
            def fcall(*args, **kwargs):
                if has_self:
                    actual_args = args[1:]
                else:
                    actual_args = args

                cache_key = fcall.make_cache_key(*actual_args, **kwargs)
                cache_data_map[cache_key] = fcall.nocache(*args, **kwargs)

                value = self.get(cache_key)
                return value

            fcall.nocache = f
            fcall.make_cache_key = CacheKeyMaker(
                namespace=namespace,
                func_name=f.__name__,
                key_func=key_func)
            return fcall

        return wrapper

    def get(self, key):
        print "get from memcache"
        return cache_data_map[key]


class CacheKeyMaker(object):
    def __init__(self, namespace, func_name, key_func):
        self.namespace = namespace
        self.func_name = func_name
        self.key_func = key_func

    def __call__(self, *args, **kwargs):
        print self.key_func.__name__
        print self.namespace
        print self.func_name
        print args[0]
        cache_key = self.key_func(
            self.namespace,
            self.func_name,
            *args,
            **kwargs)
        return cache_key


mc = MemCache()


def _key_func(namespace, f, resource_id):
    return "{}:{}".format(f, resource_id)


class KmSkuCard():
    def __init__(self, resource_id):
        self.sku = self._tsku_basic(resource_id)

    @mc.cache(key_func=_key_func)
    def _tsku_basic(self, resource_id):
        return resource_id


if __name__ == '__main__':
    card = KmSkuCard(111)
    print card.sku
