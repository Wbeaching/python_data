# -*- coding: utf-8 -*-
import scrapy


class BaiduspiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'baiduspider' #一定要存在
    # 允许爬虫的范围
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        # body 为响应体 不是html body标签
        # print(response.body)
        print(response.headers)
        # print(response.status)
