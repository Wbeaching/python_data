import requests
import xlwt
from bs4 import BeautifulSoup
import sqlite3
from fake_useragent import UserAgent
class MeiShiDB(object):
    connect = None
    curosor = None
    def openDB(self):
        self.connect = sqlite3.connect('meishiDB')
        self.curosor = self.connect.cursor()
        self.curosor.execute('create table if not exists MeishiTable (name text,src text)')
        self.connect.commit()
    def add_info_to_db(self,name,src):
        self.curosor.execute('insert into MeiShiTable(name,src) VALUES ("{}","{}")'.format(name,src))
        self.connect.commit()
    def close_DB(self):
        self.curosor.close()
        self.connect.close()
class MeiShiJie(object):
    def __init__(self):
        self.headers =UserAgent
        self.DB = MeiShiDB()

    def start_load(self):
        self.DB.openDB()
        self.get_code_with_url('')
    def get_code_with_url(self,url):
        headers = {
            'User-Agent':self.headers.random
        }
        response = requests.get(url,headers=headers).text
        code = BeautifulSoup(response,'lxml')
        self.get_content_with_code(code)
    def get_content_with_code(self,code):
        divList = code.select('div.listtylel')
        for div in divList:
            img_alt = div.select('img')[0]['alt']
            img_src = div.select('img')[0]['src']
            self.DB.add_info_to_db(img_alt,img_src)
        self.get_next_page_with_code(code)
    def get_next_page_with_code(self,code):
        next_url = code.select('a.next')
        if len(next_url) == 0:
            print('最后一页')
            return
        self.get_code_with_url(next_url[0]('href'))
meishi = MeiShiJie()
meishi.start_load()

