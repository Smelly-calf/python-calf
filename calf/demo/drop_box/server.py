#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
输出 15GB 大小的文件
反序列化 config.json，获取client端状态，判断完成之后继续输出下一个文件
源文件路径：屏幕录制 2018-12-18 11.32.28.mov  ：319.5 MB
"""
from calf.demo.utils import sync_utils
from calf.basic.file_io import this_path

file_path = "/Users/wangqian/Movies"
input_name = "屏幕录制 2018-12-18 11.32.28.mov"
out_name = "drop_box_output.mov"
config_json = this_path + "/drop_box/config.json"


def output():
    with open(file_path + "/" + input_name,'r') as fin:
        try:
            process = 0
            for li in fin.read():
                line = fin.readline()
                process += 1
                with open(file_path + "/" + out_name, 'w') as fou:
                    fou.write(line)
                if process % 12000 ==0:
                    print("process: {} %".format(process))
        except Exception as e:
            print(e)


def main():
    # 读取client端的状态 并置空 config
    with open(config_json, 'r') as conf:
        try:
            config = conf.read()
            configDict = sync_utils.unserialize(config)
            if 'status' in configDict:
                # 置空 config
                with open(config_json, 'w') as conf:
                    conf.write("{}")
                status = configDict['status']
                if status == "success":
                    output()
            else:
                output()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
