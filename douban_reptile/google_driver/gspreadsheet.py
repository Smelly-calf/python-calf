import pandas as pd
from functools import partial
import os
import pygsheets

if __name__ == '__main__':
    current_path = partial(os.path.join, os.path.dirname(__file__))
    authorize_file = current_path('hold traffic bi-5f2a76076eda.json')
    gc = pygsheets.authorize(service_file=authorize_file)
    print gc.drive, gc.oauth, gc.sheet, gc.logger, gc.teamDriveId

    # open the google spreadsheet ('pysheeetsTest' exists)
    sh = gc.open(u'保量数据可视化')
    print sh.url

    # select the first sheet
    wks = sh[0]
    result = []
    df = pd.DataFrame(result,
                      columns=['素材 id', '课程名称', '跳转 url', '保量日期', '曝光', '点击', 'CTR', '总 deal', '会员 deal', '总 OPM',
                               '会员 OPM'])
    wks.set_dataframe(df, (1, 1))

    # select the second sheet
    wks = sh[1]
    result = []
    df = pd.DataFrame(result, columns=['课程名称', '上架时间', '曝光', '点击', 'CTR', ' 总 deal', '会员 deal', '总 OPM', '会员 OPM'])
    wks.set_dataframe(df, (1, 1))