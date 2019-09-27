#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BowInvertedIndexEngine 模型实现
倒序索引
多个query的索引交集
缓存
"""
import re
import pylru

from calf.search_engine.search_engine_base import SearchEngineBase, main


class BowInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BowInvertedIndexEngine, self).__init__()
        self.inverted_index = {}

    def process_corpus(self, id, text):
        """
        text to words and save to inverted_index: key:word, value:file_paths
        :param id: file_path
        :param text: text
        """
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(id)

    def search(self, query):
        """
        注意：获取 query_words 索引数组 交集
        :param query: input query
        :return:
        """
        query_words = list(self.parse_text_to_words(query))

        result = []
        for query_word in query_words:
            if not query_word in self.inverted_index:
                return []
            result.append(self.inverted_index[query_word])
        return reduce(lambda x, y: x.intersect(y), result)

    @staticmethod
    def parse_text_to_words(text):
        # 去除标点和换行符
        text = re.sub(r'[^\w]', ' ', text)

        # 转小写
        text = text.lower()

        # 生成单词列表
        word_list = text.split(' ')

        # 去除空白单词
        word_list = filter(None, word_list)

        # 返回单词 set
        return set(word_list)


class LRUCache(object):
    def __init__(self, size=32):
        self.cache = pylru.lrucache(size)

    def has(self, key):
        return key in self.cache

    def get(self, key):
        return self.cache['key']

    def set(self, key, value):
        self.cache[key] = value


class BowInvertedIndexEngineWithCache(BowInvertedIndexEngine, LRUCache):
    def __init__(self):
        super(BowInvertedIndexEngineWithCache, self).__init__()
        LRUCache.__init__(self)

    def search(self, query):
        if self.has(query):
            print('cache hit!')
            return self.get(query)
        result = super(BowInvertedIndexEngineWithCache, self).search(query)
        self.set(query, result)

        return result


search_engine = BowInvertedIndexEngineWithCache()
main(search_engine)
