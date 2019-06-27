#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup as bs

movie_list_url = 'https://movie.douban.com/nowplaying/hangzhou/'
subject_url  = 'https://movie.douban.com/subject/'

class DouBanSpider(object):
    """
    use to reptile top25 douban movie's review score
    """
    @classmethod
    def getNowPlayingMovie_list(cls):
        """
        first step: get html_data
        :return: html_data
        """
        resp = request.urlopen(movie_list_url)
        html_data = resp.read().decode('utf-8')

        soup = bs(html_data, 'html.parser')
        nowplaying_movie = soup.find_all('div', id='nowplaying')
        nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')

        nowplaying_list = []
        # get all list-item's id and name
        for item in nowplaying_movie_list:
            nowplaying_dict = {}
            nowplaying_dict['id'] = item['data-subject']
            # get 'alt' tags as name from all tags of img
            for tag_img_item in item.find_all('img'):
                nowplaying_dict['name'] = tag_img_item['alt']
                nowplaying_list.append(nowplaying_dict)

        return nowplaying_list


    @classmethod
    def getCommentsById(cls, movieId, pageNum):
        """

        :param nowplaying_list:
        :return: comment_div_lits: div标签和comment属性下面的html代码 集合
        """
        eachCommentList = []
        if pageNum>0:
            start = (pageNum-1) * 20
        else:
            return False
        requrl = subject_url + movieId + '/comments' +'?' +'start=' + str(start) + '&limit=20'
        resp = request.urlopen(requrl)
        html_data = resp.read().decode('utf-8')
        soup = bs(html_data, 'html.parser')
        comment_div_lits = soup.find_all('div', class_='comment')

        for item in comment_div_lits:
            if str(item.find_all('p')[0]):
                eachCommentList.append(str(item.find_all('p')[0]))

        return eachCommentList





