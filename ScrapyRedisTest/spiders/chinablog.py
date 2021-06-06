# _*_ coding: utf-8 _*_
# @Time : 2021/3/31 15:18
# @File : chinablog.py
# @Author : yjh
# @Software: PyCharm


from scrapy_redis.spiders import RedisSpider
from scrapy import Request


class ChinaBlogSpider(RedisSpider):
    name = 'chinablog'
    allowed_domains = ['www.oschina.net']
    redis_key = "chinablog:start_urls"

    def parse(self, response):
        with open("a.html", "w", encoding="utf-8") as f:
            f.write(response.text)

        yield Request(url="https://www.oschina.net/", callback=self.detail)

        pass

    def detail(self, response):

        with open("b.html", "w", encoding="utf-8") as f:
            f.write(response.text)

        pass
