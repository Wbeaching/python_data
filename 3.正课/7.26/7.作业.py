# 1. 美食杰网站爬取菜谱名及人气，以 “莴笋炒蛋（2047人气）“ 形式打印
# 2.斗鱼直播网站   爬取  “分类“ 页面的全部图片和名字
#    爬取“游戏”页面的全部图片和名字
# 3.美食杰作业爬取的数据存入数据库，斗鱼作业爬取的数据保存到Excel表格
import shutil,os
import re
import sqlite3
from bs4 import BeautifulSoup
from urllib.request import Request,urlopen,urlretrieve
class DBManager(object):
    connect = sqlite3.connect('okDB')
    cursor = connect.cursor()
    @classmethod
    def create_table(cls):
        cls.cursor.execute('CREATE TABLE if NOT EXISTS mytable(name text ,pinglun text, href text)')
        cls.connect.commit()
    @classmethod
    def insert_data(cls,image_alt,pinglun,image_src):
        cls.cursor.execute('insert into mytable (name,pinglun,href) VALUES ("{}","{}","{}")'.format(image_alt,pinglun,image_src))
        cls.connect.commit()
    @classmethod
    def close_DB(cls):
        cls.cursor.close()
        cls.connect.close()
class Image_download(object):
    def __init__(self):
        self.base_url = 'https://www.meishij.net/chufang/diy/'
        self.current_page = 1
        self.total_page = 1
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    def start_spider(self):
        if os.path.exists('tupian'):
            shutil.rmtree('tupian')
        os.mkdir('tupian')
        os.chdir('tupian')
        first_page = '?&page=1'
        self.get_page_code_with_url(first_page)
    def get_page_code_with_url(self,url):
        full_url = self.base_url+url
        # print(full_url)
        request = Request(full_url,headers=self.headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('请求失败',e)
        else:
            self.get_data_with_code(code)
    def get_data_with_code(self,code):
        print('正在下载第{}页...'.format(self.current_page))
        soup = BeautifulSoup(code,'lxml')
        page_name = 'Page{}'.format(self.current_page)
        os.mkdir(page_name)
        os.chdir(page_name)
        image_list = soup.select('div.listtyle1 a')
        for image in image_list:
            image_src = image.img['src']
            image_alt = image.img['alt']+'.jpg'
            pinglun = image.div.span.string.split(' ')[3]
            print(pinglun)
            print(image_src)
            print(image_alt)
            urlretrieve(image_src,image_alt)
            DBManager.insert_data(image_alt,pinglun, image_src)
        os.chdir(os.path.pardir)
        self.current_page += 1
        self.get_next_page(code)
    def get_next_page(self,code):
        soup = BeautifulSoup(code,'lxml')
        next_page = soup.select('a.next')[0]
        url = next_page.get('href')
        # print(url)
        self.get_page_code_with_url(url)
DBManager.create_table()
download = Image_download()
download.start_spider()
DBManager.close_DB()


