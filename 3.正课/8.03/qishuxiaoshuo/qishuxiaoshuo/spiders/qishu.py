# -*- coding: utf-8 -*-
import scrapy
from .. items import QishuxiaoshuoItem

class QishuSpider(scrapy.Spider):
    name = 'qishu'
    allowed_domains = ['qisuu.la']
    start_urls = ['https://www.qisuu.la/']
    def parse(self, response):
        # print(response.text)
        # 获取导航页面所有的小说类型
        type_list = response.xpath('//div[@class="nav"]/a/@href').extract()
        # print(type_list)
        # 列表里面第一个是首页 将其去掉
        del type_list[0]
        # print(response.url)
        for type in type_list:
            # 拼接每一个类型的url
            # 在这个方法里面response.url为start.urls
            url = response.url+type[1:]
            yield scrapy.Request(url=url,callback=self.get_content_with_type_url)
            yield scrapy.Request(url=url, callback=self.get_next_page_url)
     # 用来找到每一种类型对应的内容
    def get_content_with_type_url(self,response):
        # print('-----------')
        # print(response.text)
        # 找到类型中 第一页 所有小说详情页地址
        book_list = response.xpath('//div[@class="listBox"]/ul/li/a/@href').extract()
        # print('------------')
        # print(book_list)
        for book in book_list:
            # 在这个方法里面response.url 为http://ww.qiushi.la/soft/soft0(x)/
            url = 'https://www.qisuu.la'+book
            yield scrapy.Request(url=url,callback=self.get_detail_with_book_url)
    def get_detail_with_book_url(self,response):
        item = QishuxiaoshuoItem()
        # 获取小说标题
        name = response.xpath('//div[@class="detail_right"]/h1/text()').extract_first('')
        print('----------------------------')
        # print(name)
        info_list = response.xpath('//div[@class="detail_right"]/ul/li/text()').extract()
        # 获取小说点击量
        clickNum = info_list[0]
        # 获取小说大小
        fileSize = info_list[1]
        # 获取小说类型
        bookType = info_list[2]
        # 获取更新时间
        updateTime = info_list[3]
        # 获取更新状态
        bookStatus = info_list[4]
        # 获取小说作者
        bookAuthor = info_list[5]
        # 获取需要下载的小说图片地址
        imageUrl = response.xpath('//div[@class="detail_pic"]/img/@src').extract_first('')
        imageUrl = 'https://www.qisuu.la'+imageUrl
        print(imageUrl)
        # 获取小说下载地址
        downLoad = response.xpath('//div[@class="showDown"]/ul/li[3]/script').extract_first('').split(',')[1].strip("'")
        # print(downLoad)
        item['name'] = name
        item['clickNum'] = clickNum
        item['fileSize'] = fileSize
        item['bookType'] = bookType
        item['updateTime'] = updateTime
        item['bookStatus'] = bookStatus
        item['bookAuthor'] = bookAuthor
        item['imageUrl'] = [imageUrl]
        item['downLoad'] = [downLoad]
        yield item
    def get_next_page_url(self,response):
        next_page = response.xpath('//div[@class="tspage"]/a[text()="下一页"]/@href').extract()[0]
        url = 'https://www.qisuu.la'+next_page
        yield scrapy.Request(url=url,callback=self.get_content_with_type_url)


