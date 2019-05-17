# -*- coding: utf-8 -*-
import scrapy
import re

class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['tieba.baidu.cn']
    start_urls = ['https://tieba.baidu.com/p/5815118868']
    f = open('tieba.txt','a',encoding='utf-8')
    def parse(self, response):
        # info = response.content
        # 找到指定类名的div标签  该标签内贴吧内容和作者的集合体
        tag_list = response.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')
        # print(tag_list)
        for tag in tag_list:
            # 获取含有louzhubiaoshi_wrap类名的标签
            # 该类名只有楼主才有
            author = tag.xpath('/div[@class="louzhubiaoshi_wrap"]').extract()
            if len(author) != 0:
                # 获取标签内部文本的几种方式
                # 1.获取最外层标签，遍历内部所有的子标签，获取标签文本
                # content_list = tag.xpath('.//div[@class="d_post_cotent j_d_post_content "]//text()')
                # content1 = ''
                # for content in content_list:
                #     content1+=content
                # 2.正则去掉所有标签<.*?> re.compile.sub
                # pattern = re.compile(r'<div.*?class="d_post_cotent j_d_post_content ">(.*?)</div>')
                # content_list = pattern.findall(response.text)
                # # print(content)
                # remove = re.compile('<.*?>')
                # content2 =''
                # for content in content_list:
                #     content1 = re.sub(remove,'',content)
                #     content2  += content1
                # 3./text() 获取标签的文本 //text() 获取标签文本和子标签文本
                # 4.使用xpath('string(.)')这种方式获取所有文本并且拼接
                content_list = tag.xpath('.//div[@class="d_post_content j_d_post_content "]').xpath('string(.)').extract()[0]
                # self.f.write(content)
                remove = re.compile('\s')
                douhao = re.compile(',')
                content = ''
                for string in content_list:
                    string = re.sub(remove,'',string)
                    string = re.sub(douhao,'',string)
                    content+=string
                self.f.write(content)
                self.f.write('\n')