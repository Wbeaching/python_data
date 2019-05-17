# -*- coding: utf-8 -*-
import scrapy
from .. items import HongxiuxiaoshuoItem

class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['hongxiu.com']
    start_urls = ['https://www.hongxiu.com/all']
    def parse(self, response):
        div_list = response.xpath('//div[@class="inner-wrap"]/div[@class="site"]/a/@href').extract()
        for div in div_list:
            url = 'https://www.hongxiu.com'+div
            yield scrapy.Request(url=url,callback=self.get_type_with_url)
    def get_type_with_url(self,response):
        li_list = response.xpath('//div[@class="work-filter type-filter"]/ul/li/a/@href').extract()
        for type in li_list:
            url = 'https://www.hongxiu.com/'+type[1:]
            yield scrapy.Request(url=url,callback=self.get_href_with_url)
    def get_href_with_url(self,response):
        book_href = response.xpath('//div[@class="book-info"]/h3/a/@href').extract()
        for href in book_href:
            url = 'https://www.hongxiu.com/'+href
            yield scrapy.Request(url=url,callback=self.get_content_with_url)
    def get_content_with_url(self,response):
        item = HongxiuxiaoshuoItem()
        src = 'http:'+ response.xpath('//div[@class="book-img"]/a/img/@src').extract()[0].strip('\r')
        name = response.xpath('//div[@class="book-info"]/h1/em/text()').extract()[0]
        span_list = response.xpath('//div[@class="book-info"]/p[@class="total"]/span/text()').extract()
        em_list = response.xpath('//div[@class="book-info"]/p[@class="total"]/em/text()').extract()
        zishu = span_list[0]+em_list[0]
        shoucang = span_list[1]+em_list[1]
        dianji = span_list[2]+em_list[2]
        jianjie = response.xpath('//div[@class="book-info"]/p[@class="intro"]/text()').extract()[0].strip('\n').strip('\r')
        print(jianjie)
        item['src']= [src]
        item['name'] = name
        item['zishu'] = zishu
        item['shoucang'] = shoucang
        item['dianji'] = dianji
        item['jianjie'] = jianjie
        yield item
