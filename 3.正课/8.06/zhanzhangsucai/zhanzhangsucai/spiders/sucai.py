# -*- coding: utf-8 -*-
import scrapy
from .. items import ZhanzhangsucaiItem

class SucaiSpider(scrapy.Spider):
    name = 'sucai'
    allowed_domains = ['sc.chinaz.com']
    start_urls = ['http://sc.chinaz.com']
    def parse(self, response):
        tubiao = response.xpath('//div[@class="png_tag"]/a/@href').extract()[2]
        url = self.start_urls[0]+tubiao
        yield scrapy.Request(url=url,callback=self.get_type_with_url)
    def get_type_with_url(self,response):
        type_list = response.xpath('//ul[@class="pngblock pks imgload"]/li/span/a/@href').extract()
        for type in type_list:
            yield scrapy.Request(url=type,callback=self.get_content_with_type)
    def get_content_with_type(self,response):
        item = ZhanzhangsucaiItem()
        div_list = response.xpath('//div[@class="png_sl"]/div/img/@src').extract()
        for src in div_list:
            item['src'] = [src]
            yield item






