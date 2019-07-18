#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='main',
      version='0.0.1',
      license='PRIVATE',
      author='serenity',
      author_email='serenity.yinan@gmail.com',
      description='matrix jobs',
      url='',
      packages=find_packages(exclude=['tests']),
      zip_safe=False,
      install_requires=[
          'bobo',
          'six',
          'bs4',
          'jieba',
          'numpy',
          'ipython',
          'pygsheets',
          'pandas',
      ],
      entry_points={
          'console_scripts': [
              'douban_spider = douban_reptile.movie_review.clean_data:main',
          ],
      })
