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


def mydecorator(func):
    def wrapper():
        print("wrapper of decorator.")
        func()

    return wrapper


def greet():
    print("Hello world.")


# mydecorator 是一个装饰器，把 greet 函数包裹在其中。
greet = mydecorator(greet)


# greet()


# 使用语法糖使表达更简洁
@mydecorator
def greet():
    print("Hello world.")


greet()
# 打印函数信息:'wrapper'
print(greet.__name__)


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("wrapper of my_decorator")
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(param):
    print("hello param {}".format(param))


greet("哈")
# 打印函数信息:'greet'
print(greet.__name__)
