# -*- coding: utf-8 -*-
import scrapy
from ..items import QiushibaikeItem
import re
class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/imgrank']
    f = open('content.json','a',encoding='utf-8')
    def parse(self, response):
        div_list = response.xpath('//div[@class="col1"]')
        # print(div_list)
        for div in div_list:
            item = QiushibaikeItem()
            content_list = div.xpath('.//a[@class="contentHerf"]/div[@class="content"]/span/text()').extract()
            # print(content_list)
            remove = re.compile('\n')
            for content in content_list:
                content1 = re.sub(remove,'',content)+'\n'
                self.f.write(content1)
                # item['content1'] = content1
                # print(content1)
            img_list = div.xpath('.//div[@class="thumb"]/a/img/@src').extract()
            # print('---------------------------------------')
            # print(img_list)
            for img in img_list:
                img = 'http:'+img
                item['img'] = [img]
                yield item
        next_url = response.xpath('//ul[@class="pagination"]/li/a/@href').extract()[-1]
        url = 'https://www.qiushibaike.com/imgrank'+next_url
        print('---------------------------------')
        print(url)
        yield scrapy.Request(url=url,callback=self.parse)