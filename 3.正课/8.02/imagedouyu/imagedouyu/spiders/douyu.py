# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import ImagedouyuItem
class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['api.douyucdn.cn']
    base_url = 'http://api.douyucdn.cn/api/v1/getverticalRoom?limit=20&offset='
    offset = 0
    start_urls = [base_url+str(offset)]

    def parse(self, response):
        jesonData = json.loads(response.text)
        print(jesonData)
        if len(jesonData['data']) != 0:
            for image in jesonData['data']:
                item = ImagedouyuItem()
                src= image['room_src']
                print(src)
                # 使用管道文件下载图片的话，需要将内容包裹到列表中
                item['src'] =[src]
                # 传递item到管道文件
                yield item
            self.offset+=20
            url = self.base_url+str(self.offset)
            yield scrapy.Request(url=url,callback=self.parse)


