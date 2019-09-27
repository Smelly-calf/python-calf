#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def get_FileSize(filePath):
    filePath = unicode(filePath, 'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)
