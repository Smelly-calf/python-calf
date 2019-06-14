#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jieba    #分词包
import matplotlib as matplotlib
import pandas as pd

from douban_reptile.movie_review.spider_html import DouBanSpider
import re
import numpy as np
from wordcloud import WordCloud#词云包

import warnings
warnings.filterwarnings("ignore")
import codecs   #codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode

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
        words_df=pd.DataFrame({'segment':segment})

        # except not use words
        # stopwords=pd.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')#quoting=3全不引用
        # words_df=words_df[~words_df.segment.isin(stopwords.stopword)]

        # statistics word cnt
        words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":np.size})
        words_stat=words_stat.reset_index().sort_values(by=["计数"],ascending=False)

        return words_stat



if __name__ == '__main__':
    commentList = []
    NowPlayingMovie_list = DouBanSpider.getNowPlayingMovie_list()
    for i in range(10):
        num = i + 1
        commentList_temp = DouBanSpider.getCommentsById(NowPlayingMovie_list[0]['id'], num)
        commentList.append(commentList_temp)

    cleaned_comments = CleanData.clean_comments(commentList)
    print(cleaned_comments)
    words_stat = CleanData.word_fre_stats(cleaned_comments)

    # 使用词云显示
    wordcloud=WordCloud(font_path="simhei.ttf",background_color="white",max_font_size=80)
    word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}

    word_frequence_list = []
    for key in word_frequence:
        temp = (key,word_frequence[key])
        word_frequence_list.append(temp)

    print(dict(word_frequence_list))

    wordcloud=wordcloud.fit_words(dict(word_frequence_list))
    # plt.imshow(wordcloud)