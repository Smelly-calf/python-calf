#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from bs4 import BeautifulSoup as bs

content = "<video id='None' data-swfurl='' poster='https://pic1.zhimg.com/v2-149e4ace28d16129279501cbc0939d23_r.jpg'  data-name='手机能拍月亮么？' data-video-id='1078308507979362304' data-video-playable='true' data-lens-id='1078308507979362304' data-paid-video-play-url='zhihu://km/video_player/1078308507979362304?resource_id=1073545024410652672&section_id=1078308507979362304&extra_auto_play=true&play_start=0'></video>"

# data-sourceurl='https://www.zhihu.com/video/1078308507979362304'
replacement = "poster:1234"

MarketResourceType = {
    1: "Live",
    2: "LiveCourse",
    3: "LiveSpecial",
    4: "RemixAlbum",
    5: "Ebook",
    6: "EbookAudio",
    7: "RemixInstabook",
    8: "PaperBook",
    9: "Special",
    10: "PaidMagazine",
    11: "Bundle",
    12: "Paid_Column"
}

MarketResourceSubType = {
    (4, 0): "音频",
    (4, 1): "视频",
    (5, 0): "外采",
    (5, 1): "未知",
    (5, 2): "周刊",
    (5, 3): "一小时",
    (5, 4): "有声书"
}

question_ids = [1, 2, 3, 4]
if __name__ == '__main__':
    # soup = bs(content, 'html.parser')
    # video = soup.find_all('video')[0]
    # video['poster']=replacement
    # print(video.get('data-test-haha'))
    # print(video)
    # print(soup)
    # print(type(str(soup)))
    # print(content)

    # soup = bs(content, 'html.parser')
    # for video in soup.select('video'):
    #     print(video)
    #     video.replace_with(bs(replacement.format(text=video.text), 'html.parser'))
    # print(soup)
    # video.replace_with(bs(replacement.format(text=video['poster']), 'html.parser'))
    # print(MarketResourceSubType.get((4, 0)))
    resource_type = 4
    resource_sub_type = 0
    resource_sub_type = MarketResourceSubType.get((resource_type, resource_sub_type))
    print(resource_sub_type)

    question_cnt = {}

    for question_id, cnt in [(1, 2), (2, 1)]:
        question_cnt[int(question_id)] = {"paid_answer_num": cnt}
    print (question_cnt)

    for question_id, answer_num in [(1, 4), (2, 2), (3, 1)]:
        if question_id in question_cnt.keys():
            question_cnt[question_id].update({"answer_num": answer_num})
        else:
            question_cnt[question_id] = {"answer_num": answer_num}
    print (question_cnt)
    print(question_cnt[1].get("paid_answer_num"))
    print(question_cnt[3].get("paid_answer_num"))


    # print(tuple([question_id for question_id in question_ids]))
    # print(tuple(question_ids))
