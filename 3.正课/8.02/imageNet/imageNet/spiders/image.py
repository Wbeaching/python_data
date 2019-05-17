# -*- coding: utf-8 -*-
import scrapy
from ..items import ImagenetItem


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/4kmeishi/']

    def parse(self, response):
        img_list = response.xpath('//ul[@class="clearfix"]/li/a/img/@src')
        # print(img_list)
        for img in img_list:
            # 使用在items.py中创建的模型
            item = ImagenetItem()
            # 拼接url，得到完整的下载地址
            src= 'http://pic.netbian.com'+img.extract()
            # 将得到的下载地址，放入到数据模型中
            # 下载得治腰包在列表当中
            item['src']=[src]
            # 将数据模型传给管道
            yield item

        next_url = response.xpath('//div[@class="page"]/a[text()="下一页"]/@href').extract()
        print(next_url)
        if len(next_url) !=0:
            url = 'http://pic.netbian.com'+next_url[0]
            # 将scrapy.Rquest 得到的结果继续用self.parse记性处理
            # callback 回调
            yield scrapy.Request(url=url,callback=self.parse)