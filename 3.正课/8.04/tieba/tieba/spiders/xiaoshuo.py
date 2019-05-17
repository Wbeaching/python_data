# -*- coding: utf-8 -*-
import scrapy
import re

class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/p/5815118868']
    f= open('content.txt','a',encoding='utf-8')
    def parse(self, response):
        # print(response.text)
        div_list = response.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')
        # print(div_list)
        for div in div_list:
            author = div.xpath('.//div[@class="louzhubiaoshi_wrap"]').extract()
            # print(author)
            if len(author) != 0:
                # # 获取文本的几种方式？
            # ---------------------------------------------------------
                # content_list = div.xpath('.//div[@class="d_post_content j_d_post_content "]/text()').extract()
                # # print(content_list)
                # content = ''
                # remove = re.compile('\s')
                # douhao = re.compile(',')
                # for string in content_list:
                #     string = re.sub(remove,'',string)
                #     string = re.sub(douhao,'',string)
                #     content+=string+'\n'
                # print(content)
                # self.f.write(content)
            # -------------------------------------------------------
                # content_list = div.xpath('.//div[@class="p_content  "]//text()').extract()
                # print(content_list)
                # content = ''
                # remove = re.compile('\s')
                # douhao = re.compile(',')
                # for string in content_list:
                #     string = re.sub(remove,'',string)
                #     string = re.sub(douhao,'',string)
                #     content+=string+'\n'
                # # print(content)
                # self.f.write(content)
            # ---------------------------------------------------------
            #     content_list = div.xpath('.//div[@class="p_content  "]/cc/div').extract()
            #     br = re.compile(r'<.*?>')
            #     remove = re.compile('\n')
            #     kouge = re.compile('\s')
            #     content =''
            #     for string in content_list:
            #         string = re.sub(br,'',string)
            #         string = re.sub(remove,'',string)
            #         string = re.sub(kouge,'',string)
            #         content+=string+'\n'
            #     print(content)
            #     self.f.write(content)
        # -----------------------------------------------------------------
# (4)string(.)获取文本直接拼接文本
                content = div.xpath('.//div[@class="p_content  "]').xpath('string(.)').extract_first()
                print(content)
                kouge = re.compile('\s')
                content = re.sub(kouge,'',content)+'\n'
                print(content)
                self.f.write(content)










