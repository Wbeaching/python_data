import xlwt
import random
import requests
from lxml import etree
from fake_useragent import UserAgent
from urllib.request import ProxyHandler,build_opener
class DBMovie(object):
    def __init__(self):
        self.base_url ='https://movie.douban.com/top250'
        self.current = 1
        self.headers = UserAgent()
        self.sheet = None
        self.workBook = None
        self.record = 1
    def start_load_dbmovie(self):
        self.get_excel()
        # 第一次调用，不用传值
        self.get_code_with_url()
        self.workBook.save('豆瓣top250.xls')
    def get_excel(self):
        self.workBook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workBook.add_sheet('电影排行榜')
        self.sheet.write(0, 0,'排名')
        self.sheet.write(0, 1, '影片')
        self.sheet.write(0 ,2, '导演和演员')
        self.sheet.write(0 ,3,'评分')
        self.sheet.write(0, 4, '评论人次')

    def get_code_with_url(self,url):
        # 随机选择一个用户标识
        headers = {
            'User-Agent':self.headers.random
        }
        ip_list = [
            '101.236.23.202:8866',
            '61.135.217.7:80',
            '111.155.116.234:8123',
            '122.114.31.177:808'
        ]
        proxies = {
            'http:': random.choice(ip_list)
        }
        full_url = self.base_url + url
        proxy_handler = ProxyHandler(proxies)
        opener = build_opener(proxy_handler)
        response = requests.get(full_url,headers = headers).text
        print(response)
        code = etree.HTML(response)
        item_div = code.xpath('//div[@class="item"]')
        for tag in item_div:
            # . 表示从当前节点开始
            # ..表示从父节点开始
            rank = tag.xpath('.//em[@xlass=""]/text()')[0]
            print(rank)
            movie_name = tag.xpath('.//div[@class="hd"]/a/span/text()')
            print(movie_name)
            name = ''
            for movie in movie_name:
                name +=movie
            print(name)
            creater = tag.xpath('.//div[@class="bd"]/p[@class=""]/text()'[0])
            creater = creater.strip('\n').repla1ce(' ','')
            print(creater)
            start = tag.xpath('.//span[@class="rating_num"]/text()')[0]
            print(start)
            comment_num = tag.xpath('.//div[@class="start"]/span[last()]/text()')[0]
            comment_num = comment_num[0:-3]
            print(comment_num)
            self.sheet.write(self.record, 0, rank)
            self.sheet.write(self.record, 1, name)
            self.sheet.write(self.record, 2, creater)
            self.sheet.write(self.record, 3, start)
            self.sheet.write(self.record, 4, comment_num)
            self.record+=1
            self.get_next_page(code)
    def get_next_page(self,code):
        next_url = code.xpath('//span[@class="next"]/a/@href')
        if len(next_url) == 0:
            print('已经是最后一页')
            return
        self.get_code_with_url(next_url[0])
movie = DBMovie()
movie.start_load_dbmovie()