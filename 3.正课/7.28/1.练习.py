import requests,os,shutil
from bs4 import BeautifulSoup
from lxml import etree
from urllib.request import urlretrieve
import sqlite3
# connect = sqlite3.connect('新闻')
# curosr = connect.cursor()
# curosr.execute('create table if not  exists mytable(name text,href text)')
# connect.commit()
# url = 'http://news.baidu.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
# }
# response = requests.get(url,headers = headers).content
# # print(response)
# soup = BeautifulSoup(response,'lxml')
# # print(soup)
# new_list = soup.select('ul.focuslistnews li a')
# # print(new_list)
# for news in new_list:
#     href = news.get('href')
#     text = news.get_text()
#     # print(href)
#     # print(text)
#     print('新闻：'+text+'；链接：'+href)
#     curosr.execute('insert into mytable(name,href) VALUES ("{}","{}")'.format(text,href))
#     connect.commit()
# curosr.close()
# connect.close()
# beautifulsoup是python的一个第三方库
# 和xpath作用一样，都是用来解析数据的
# xpath比较快
# xpath底层是用c实现的
# beautiful里面需要两个参数
# 1. open 2.固定写法lxml
# response = requests.get(url).content
# soup = BeautifulSoup(response,'lxml')
# response = requests.get(url).content
# code = etree.HTML(response)
# bs = BeautifulSoup(open('',encoding='utf-8'))
# print(bs)
# print(type(bs))
# # 获取网页中的title标签
# print(bs.title)
# # 获取网页中第一个a标签
# print(bs.a)
# # 获取当前内容的标签名
# print(bs.name)
# print(bs.head.name)
# print(bs.title.name)
# print(bs.a['id'])
# print(bs.a['href'])
# print(bs.a['class'])
# print(bs.html['lang'])
# del bs.a['id']
# print(bs.a)
# # 获取本标签中的文本
# print(bs.a.string)
# print(bs.div.string)
# # 获取指定标签中的内容
# print(bs.head.contends)
# print(bs.body.contens)
# # 获取内容中指定索引的内容
# print(bs.div.contents[3])
# # 获取所有父级标签的所有标签
# head = bs.title.parent
# print(head)
# # 通过id来获取标签的内容
# print(bs.find(id="id"))
# # 找到符合的class
# print(bs.find_all(class_="shopping"))
# # 选择指定的标签
# print(bs.select('title'))
# # 获取所得a标签
# print(bs.select('a'))
# # . 表示类名 #表示id
# # 找到一个类名为now的div标签
# print(bs.select('div.now'))
class Image_downLoad(object):
    def __init__(self):
        self.base_url = 'http://www.ivsky.com/'
        self.current_page = 1
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
    def start_spider(self):
        if os.path.exists('tupian'):
            shutil.rmtree('tupian')
        os.mkdir('tupian')
        os.chdir('tupian')
        first_page = 'tupian/index_1.html'
        self.get_page_code_with_url(first_page)
    def get_page_code_with_url(self,url):
        full_url = self.base_url+url
        response = requests.get(full_url,headers =self.headers).content
        code =response.decode()
        # print(soup)
        self.get_data_with_code(code)
    def get_data_with_code(self,code):
        page_name = 'Page{}'.format(self.current_page)
        os.mkdir(page_name)
        os.chdir(page_name)
        soup = BeautifulSoup(code, 'lxml')
        image_list = soup.select('div.il_img a img')
        # print(image_list)
        for image in image_list:
            image_src = image.get('src')
            image_alt = image.get('alt').split('(')[0]+'.jpg'
            # print(image_src)
            # print(image_alt)
            urlretrieve(image_src,image_alt)
        os.chdir(os.path.pardir)
        self.current_page+=1
        self.get_next_page(code)
    def get_next_page(self,code):
        soup = BeautifulSoup(code,'lxml')
        next_page = soup.select('a.page-next')[0]
        # print(next_page)
        url = next_page.get('href')
        # print(url)
        self.get_page_code_with_url(url)
image = Image_downLoad()
image.start_spider()





