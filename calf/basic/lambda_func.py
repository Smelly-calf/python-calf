#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
简约而不简单的匿名函数：lambda
匿名函数是函数, 不是变量
lambda函数用在 常规函数不能用的地方：列表内

map(func, iterable): 返回新的可遍历的集合
filter(func, iterable)
reduce(func, iterable)

1、对字典d值由高到低排序：d={'mike':10,'lucy':2,'ben':30}
2、使用匿名函数的场景
"""
if __name__ == '__main__':
    print("请开始你的程序")
    square = lambda x: x ** 2  # 定义lambda函数 square
    square(3)  # 调用匿名函数

    d = {'mike': 10, 'lucy': 2, 'ben': 30}
    sorted_d = sorted(d, key=lambda x: -x[1])
