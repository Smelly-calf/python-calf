#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

project_dir = os.path.abspath(".")


class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception("process_corpus not implemented.")

    def search(self, query):
        raise Exception("search not implemented.")


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(project_dir + "/" + file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print("found {} results:".format(len(results)))
        for result in results:
            print(result)
