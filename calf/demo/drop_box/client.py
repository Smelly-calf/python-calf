#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
读取 5GB 大小的文件并保存
读取完成：序列化状态到 config.json
"""
import os

from calf.demo.drop_box.server import input_name
from calf.demo.utils import sync_utils
from calf.basic.file_io import this_path
from calf.demo.utils.file_utils import get_FileSize

file_path = "/Users/wangqian/Movies"
file_name = "drop_box_output.mov"
config_json = this_path + "/drop_box/config.json"
input_size = get_FileSize(file_path + "/" + input_name)


def read():
    with open(file_path + "/" + file_name, 'r') as fin:
        try:
            for li in fin.read():
                line = fin.readline()
                with open(file_path + "/" + file_name + ".mov", 'w') as fou:
                    fou.write(line)
                    # 同步状态：成功
                    if get_FileSize(file_path + "/" + file_name + ".mov") == input_size:
                        sync_utils.serialize({"status": "success"}, os.path.abspath(config_json))
        except Exception as e:
            # 同步状态：失败
            print(e)
            sync_utils.serialize({"status": "failer"}, config_json)




def main():
    read()


if __name__ == '__main__':
    main()
