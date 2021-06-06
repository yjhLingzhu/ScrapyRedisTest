# _*_ coding: utf-8 _*_
# @Time : 2021/3/11 16:44
# @File : main.py
# @Author : yjh
# @Software: PyCharm


import sys
import os

from scrapy.cmdline import execute


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# execute(["scrapy", "crawl", "jobbole"])
# execute(["scrapy", "crawl", "zhihu"])
# execute(["scrapy", "crawl", "lagou"])
execute(["scrapy", "crawl", "chinablog"])

