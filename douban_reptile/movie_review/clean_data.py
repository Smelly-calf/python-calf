#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jieba  # 分词包
import pandas as pd

from douban_reptile.movie_review.spider_html import DouBanSpider
import re
import numpy as np
from wordcloud import WordCloud  # 词云包

import warnings

warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)


class CleanData(object):
    """
    this class use to clean the html data
    """

    @classmethod
    def clean_comments(cls, eachCommentList):
        comments = ''
        for k in range(len(eachCommentList)):
            comments = comments + (str(eachCommentList[k])).strip()

        # trunc Punctuation
        pattern = re.compile(r'[\u4e00-\u9fa5]+')
        filterdata = re.findall(pattern, comments)
        cleaned_comments = ''.join(filterdata)

        return cleaned_comments

    @classmethod
    def word_fre_stats(cls, cleaned_comments):
        segment = jieba.lcut(cleaned_comments)
        words_df = pd.DataFrame({'segment': segment})

        # except not use words
        # stopwords=pd.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')#quoting=3全不引用
        # words_df=words_df[~words_df.segment.isin(stopwords.stopword)]

        # statistics word cnt
        words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": np.size})
        words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)

        return words_stat


if __name__ == '__main__':
    commentList = []
    NowPlayingMovie_list = DouBanSpider.getNowPlayingMovie_list()

    # 获取一部电影的前 10 页的评论
    for i in range(10):
        num = i + 1
        commentList_temp = DouBanSpider.getCommentsById(NowPlayingMovie_list[0]['id'], num)
        commentList.append(commentList_temp)

    # 将 list 组成字符串，后面做词云分析
    cleaned_comments = CleanData.clean_comments(commentList)

    # 单词频率统计
    words_stat = CleanData.word_fre_stats(cleaned_comments)
    word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}

    print(word_frequence)

    # 使用词云显示
    wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)
    wordcloud = wordcloud.fit_words(word_frequence)
    # plt.imshow(wordcloud)
