# -*- coding: utf-8 -*-
import scrapy
from .. items import BiantuwangtItem

class BianSpider(scrapy.Spider):
    name = 'bian'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/4kfengjing/']

    def parse(self, response):
        item = BiantuwangtItem()
        img_list = response.xpath('//ul[@class="clearfix"]/li/a/img/@src').extract()
        for img in img_list:
            url = 'http://pic.netbian.com'+img
            item['url'] = url
            yield item
        next_url = response.xpath('//div[@class="page"]/a[text()="下一页"]/@href').extract()
        if len(next_url) != 0:
            url = 'http://pic.netbian.com'+next_url[0]
            yield scrapy.Request(url=url,callback=self.parse)
