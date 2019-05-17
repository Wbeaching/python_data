# 定义一个爬虫类 需要两个参数  1个是url地址 一个是正则表达式，根据两个参数将获取的内容写入到本地数据库
# 将正则表达式获取的内容写入到数据库
# 确保在代码不修改的情况下 至少 能爬虫五个网页
# jd  taobao 百度 mi huawei

import re
from urllib.request import Request,urlopen
import sqlite3
class DBManager(object):
    connect = None
    cursor = None
    @classmethod
    def create_db_and_table(cls):
        cls.connect = sqlite3.connect('allDB')
        cls.cursor = cls.connect.cursor()
        cls.cursor.execute('create table if not exists contentdb(value text)')
        cls.connect.commit()
    @classmethod
    def insert_into_table(cls,receiveData):
        cls.connect = sqlite3.connect('allDB')
        cls.cursor = cls.connect.cursor()
        cls.cursor.execute('insert into contentdb(value) VALUES ("{}")'.format(receiveData))
        cls.connect.commit()
    @classmethod
    def close_db(cls):
        cls.cursor.close()
        cls.connect.close()

class AllSpider(object):
    def __init__(self,base_url,pattern):
        self.base_url = base_url
        self.pattern = pattern
        self.header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'
        }

    def get_code_from_url(self):
        request = Request(self.base_url,headers=self.header)
        response = urlopen(request)
        code = response.read().decode()
        return code
    def get_info_from_code(self,code):
        pattern = re.compile(r'{}'.format(self.pattern),re.S)
        result = pattern.findall(code)
        # print(result)
        for value in result:
            for receiveData in value:
                # print(receiveData)
                DBManager.insert_into_table(receiveData)

url = AllSpider('https://www.baidu.com/','<div id="u1">.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>')
# url = AllSpider()
code = url.get_code_from_url()
url.get_info_from_code(code)

DBManager.create_db_and_table()

DBManager.close_db()