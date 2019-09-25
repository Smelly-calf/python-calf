#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python 字典和集合:
字典和集合是高度优化的哈希表，均为无序;
字典通过 键值对存储，
集合中元素唯一，无序，可通过 sorted(set) 获得排好序的集合;

字典和集合 增删改查的 时间复杂度为 O(1) 常数时间内。
字典和集合 底层存储：hash表，索引和元素分开存放，提升空间效率：不同的是字典存储了 索引+键值对，集合存储 索引+value。

字典和集合，无论是键还是值，都可以是混合类型。
判断元素是否在字典/集合： key/elem in dict/set 判断元素是否在字典/集合中。

"""


def dict_operator():
    """
    字典创建的四种方式如下：
    测试每种创建方式耗时：
        python3 -m timeit 'd1 = {"key1": "value1", "key2": 1}'
        python3 -m timeit 'd2 = dict({"key1": "value1", "key2": 1})'
        结论：第一种平均 67.3 纳秒，第二种平均 229 纳秒，第一种效率高；第一种建一个hash表，第二种额外创建dict实例。

    元素访问：直接索引, 如果key 不存在 抛异常。 使用 get(key,default)如果键不存在，返回一个默认值。

    增删改操作
    """

    """
    反编译查看执行过程
    >>> import dis
    >>> def f1():return {'1':1}
    >>> def f2():return dict({'1':1})
    >>> dis.dis(f1)
      1           0 LOAD_CONST               1 ('1')
                  2 LOAD_CONST               2 (1)
                  4 BUILD_MAP                1
              6 RETURN_VALUE

    >>> dis.dis(f2)
      1           0 LOAD_GLOBAL              0 (dict)
          2 LOAD_CONST               1 ('1')
          4 LOAD_CONST               2 (1)
          6 BUILD_MAP                1
          8 CALL_FUNCTION            1
         10 RETURN_VALUE
    """

    d1 = {"key1": "value1", "key2": 1}  # 5,000,000 loops, best of 5: 67.3 nsec per loop
    d2 = dict({"key1": "value1", "key2": 1})  # 1,000,000 loops, best of 5: 229 nsec per loop
    d3 = dict([("key1", "value1"), ("key2", 1)])
    d4 = dict(key1="value1", key2=1)
    print(d1 == d2 == d3 == d4)

    # 增
    d1['key3'] = {1, 2, 3}
    # 删
    # d1.popitem()  # 无法知道删除的哪一个元素, 与集合的pop操作一致，慎用
    d1.pop('key3')
    print(d1)

    # 改
    d1['key1'] = "update"

    # 排序：排序的数据类型 必须一致
    d_sorted_by_key = sorted(d1.items(), key=lambda x: x[0])  # 键升序排序
    d1['key2'] = "value2"
    d_sorted_by_value = sorted(d1.items(), key=lambda x: x[1])  # 值升序排序
    print(d_sorted_by_key)
    print(d_sorted_by_value)


def set_operator():
    """
    set集合 创建的两种方式
    """
    s1 = {1, 2, 3}
    s2 = set([1, 2, 3])  # 直接用第一种
    print(s1 == s2)  # 返回 True，判断的是元素相等

    # 访问：集合本质上是哈希表，不支持索引操作, 通过 in 判断元素是否在集合内
    print(1 in s1)  # 返回 True

    # 增
    s1.add("5")
    # 删
    # s1.pop() # 集合的 pop 操作是删除最后一个元素，但集合是无序的，无法知道删除的是哪个元素，因此慎用
    s1.remove('5')  # 使用 remove 删除元素

    # 排序
    s1_sorted = sorted(s1, reverse=True)  # 降序
    print(s1_sorted)


def find_unique_price_using_list(products):
    """使用列表查找商品价格"""
    unique_price_list = []
    for _, price in products:
        if price not in unique_price_list:
            unique_price_list.append(price)
    return len(unique_price_list)


def find_unique_price_using_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)


def compare_performance():
    """
    列表和集合的性能
    结论：对于 100000条数据量 集合比列表快 4500 倍左右
    """
    import time

    # 100000 条数据
    id = [x for x in range(0, 100000)]
    price = [x for x in range(200000, 300000)]
    products = list(zip(id, price))

    # 统计list的时间，输出：time elapse using list:45.342015808
    start = time.perf_counter()
    find_unique_price_using_list(products)
    end=time.perf_counter()
    print("time elapse using list:{}".format(end-start))

    # 统计集合的时间，输出：time elapse using set:0.011281871999997861
    start = time.perf_counter()
    find_unique_price_using_set(products)
    end = time.perf_counter()
    print("time elapse using set:{}".format(end-start))


def main():
    # 字典操作
    # dict_operator()
    # 集合操作
    # set_operator()
    compare_performance()


if __name__ == '__main__':
    main()
