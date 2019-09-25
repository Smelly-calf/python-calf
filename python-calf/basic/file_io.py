#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python IO 和 Json 序列化

IO 处理：强制类型转换均用 try except 处理，并且避免数据溢出：int类型C++的限制是 21亿，float类型有精度限制。

该代码用来读取文件 in.txt 做 NLP(自然语言)处理，并输出到 out.txt 文件中。

所有 IO 都应该进行错误处理。
所有 序列化 和 反序列化 都要进行错误处理。

序列化：json.dump(python对象)
反序列化：json.load(json字符串)

报错：
1、write 的时候报错：ERROR:root:string index out of range
原因：sorted(word_cnt, key=lambda x: -x[1])
应该用：sorted(word_cnt.items(), key=lambda x: -x[1])

"""
import json
import logging
import os
import re

# 项目根路径
path = os.path.abspath('..')

# word_cnt 定义为全局变量
word_cnt = {}


def parse(text):
    """
    NLP 任务的基本步骤：
        1、读取文件;
        2、去除所有标点和换行符，并把所有大写变为小写;
        3、合并相同的词，统计每个词出现频率，按照词频从大到小排序;
        4、结果按行输出到文件 out.txt 中。
    :param text: str
    """

    # 去除标点和换行符
    text = re.sub(r'[^\w]', ' ', text)

    # 转小写
    text = text.lower()

    # 分割生成单词列表
    word_list = text.split(' ')

    # 去除空白单词
    word_list = filter(None, word_list)

    # 生成单词和词频的字典
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1

    # 按照词频降序排序
    # sorted_word_cnt = sorted(word_cnt.items(), key=lambda x: -x[1])

    return word_cnt


def io_and_parse():
    """
    io输入输出，以及json序列化
    :return:
    """
    # 输入：读取文件: r只读模式
    with open(path + '/resource/in.txt', 'r') as fin:
        try:
            # 输入：read_line
            text = fin.read()  # 优化：用 readLine 方法
            word_and_freq = parse(text)
        except Exception as e:
            logging.error(e)
            return

    # 输出：写出 w 只写模式
    # 1、按行写出
    with open(path + '/resource/out.txt', 'w') as fou:
        for word, freq in word_and_freq.items():
            try:
                fou.write('{}:{}\n'.format(word, freq))
            except Exception as e:
                logging.error(e.message)

    # 2、json.dump 序列化
    with open(path + '/resource/out.txt', 'w') as fou:
        try:
            json.dump(word_and_freq, fou)  # 使用json序列化
        except Exception as e:
            logging.error(e)
            return


def io_and_parse_2():
    """
    进阶版：使用 readline 方法
    """
    with open(path + '/resource/in.txt', 'r') as fin:
        try:
            # 每次处理一行
            for line in fin:
                parse(line)
        except Exception as e:
            logging.error(e)
            return

    with open(path + '/resource/out.txt', 'w') as fou:
        try:
            # 按词频从大到小排序
            sorted_word_cnt = sorted(word_cnt.items(), key=lambda x: -x[1])
            for word, cnt in sorted_word_cnt:
                fou.write('{},{}\n'.format(word, cnt))
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    io_and_parse_2()
