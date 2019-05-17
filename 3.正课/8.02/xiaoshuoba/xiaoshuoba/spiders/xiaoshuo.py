# -*- coding: utf-8 -*-
import scrapy
# from ..import XiaoshuobaItem

class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/p/5815118868/']

    def parse(self, response):
        tag_list = response.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')
        for tag in tag_list:
            # item = XiaoshuobaItem()
            name = tag.xpath('.//li[@class="d_name"]/a/text()').extract()[0]
            # print(name)
            content = tag.xpath('.//div[@class="d_post_content j_d_post_content "]/text()').extract()
            # print(content)
            # content1 = ''
            for char in content:
                if name == '乔深沉':
                    with open('xiaoshuo.txt', 'a', encoding='utf-8')as f:
                        f.write('{}'.format(char))
                        f.write('\n')
                    f.close()
            # item['name']=name
            # item['content2']=content2
            # yield item
        next_url = response.xpath('//ul[@class="l_posts_num"]/li/span[@class="tp"]/a[text()="下一页"]/@href').extract()
        # print(next_url)
        if len(next_url) != 0:
            url = 'https://tieba.baidu.com/p/5815118868' + next_url[0]
            yield scrapy.Request(url=url, callback=self.parse)