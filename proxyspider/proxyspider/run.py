#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
# @Time  : 2022/10/22 21:14:16
# @Author: wd-2711
'''

from scrapy import cmdline
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
name = 'proxyspider'
cmd = 'scrapy crawl {0}'.format(name)
print(cmd.split())
cmdline.execute(cmd.split())