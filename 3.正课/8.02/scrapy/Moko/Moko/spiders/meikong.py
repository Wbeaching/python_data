# -*- coding: utf-8 -*-
import scrapy
# 在同级文件夹路径下，找不到文件夹item
# 所以回到上级文件夹路径来找 ..回到上级路径
from ..items import MokoItem
class MeikongSpider(scrapy.Spider):
    name = 'meikong'
    allowed_domains = ['moko.cc']

    start_urls = ['http://www.moko.cc/channels/post/153/1.html']

    def parse(self, response):
        # print(response.text)
        ul_list = response.xpath('//ul[@class="post small-post"]')
        # print(ul_list)
        all_items =[]
        for ul in ul_list:
            item = MokoItem()
            # xpath获取的对象都是一个列表
            # 返回的内容为scrapy.selector
            # 如果对象类型为scrapy.selector，那么这个对象可以继续迭代
            # 也可以被xpath继续寻找里面的内容
            title = ul.xpath('.//div[@class="cover"]/@cover-text')
            # print(title)
            # print(type(title))
            # 将xpath独享转化为列表对象
            title = title.extract()[0]
            # print(title)#['美轮美奂']
            # 如果对象的类型为list，那么这个对象可以被迭代
            # 但是不能继续使用xpath
            # print(type(title))#<class list>
            # 点击量
            clickNum = ul.xpath('.//li[last()]/span/text()').extract()[0]
            # print(clickNum)
            # 图片链接
            imgSrc = ul.xpath('.//img/@src2').extract()[0]
            # print(imgSrc)
            item['title'] = title
            item['imgSrc'] = imgSrc
            item['clickNum'] =clickNum
            yield item

        # yield all_items

