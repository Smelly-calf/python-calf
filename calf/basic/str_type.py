#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    """
    时间复杂度：3>2>1
    """
    import time

    # 测试 str+=
    start_time = time.perf_counter()
    s = ''
    for n in range(0, 10000):
        s += str(n)
    end_time = time.perf_counter()
    print('Time elapse: {}'.format(end_time - start_time))
    #Time elapse: 1000：0.00042425300000004107

    # 测试 join
    start_time = time.perf_counter()
    s = []
    for n in range(0, 10000):
        s.append(str(n))
    ''.join(s)
    end_time = time.perf_counter()
    print('Time elapse: {}'.format(end_time - start_time))
    #Time elapse: 0.000397046000000012

    # 测试 map
    start_time = time.perf_counter()
    s = "".join(map(str, range(0, 10000)))
    end_time = time.perf_counter()
    print('Time elapse: {}'.format(end_time - start_time))
    #Time elapse: 0.00026137500000000813


