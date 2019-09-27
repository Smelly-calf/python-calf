#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
协程：coro(coroutine)
python 协程模块：asyncio
协程函数: 定义形式为 async def 的函数;
协程对象: 调用 协程函数 所返回的对象。

直接调用一个协程不会触发程序执行。
要真正运行一个协程，asyncio 提供了三种机制：
    1、asyncio.run(coro()) 运行最高层级的入口点:main方法
    2、await coro()， 等待一个协程
    3、asyncio.create_task(coro()), python3.7之前 asyncio.ensure_future(coro())

可等待对象 有三种主要类型：协程, 任务 和 Future
Future对象：asyncio.gather(**协程函数) 返回 Future对象

"""
import asyncio

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('Ok {}'.format(url))

