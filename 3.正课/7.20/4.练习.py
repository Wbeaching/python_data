
import re
from urllib.request import Request,urlopen
import sqlite3
# 专门处理各种数据，使其符合要求
class  dataManager(object):
    # 该方法负责修改数据，取出不必要的数据
    def update_new_data(self,oldData):
        # 去除换行
        name = oldData[0]
        name = name.strip('\n')
        content = oldData[2]
        content = content.strip('\n')
        # 去除br
        pattern = re.compile(r'<br/>')
        content = pattern.sub('',content)
        newData = (name,oldData[1],content,oldData[3],oldData[4])
        return newData
class DBManager(object):
    connect = None
    cursor = None
    @classmethod
    # 创建数据库和表
    def create_db_and_table(cls):
        cls.connect = sqlite3.connect('qbDB')
        cls.cursor = cls.connect.cursor()
        cls.cursor.execute('create table if not exists qbTable (name text,age text,content text,like text,conment text)')
        cls.connect.commit()
    @classmethod
    # 添加数据到数据库
    def insert_info_to_table(cls,receiveData):
        cls.cursor.execute('insert into qbTable(name,age,content,like,conment) VALUES ("{}","{}","{}","{}","{}")'.format(receiveData[0],receiveData[1],receiveData[2],receiveData[3],receiveData[4]))
        cls.connect.commit()
    @classmethod
    # 关闭数据库
    def close_qb(cls):
        cls.cursor.close()
        cls.connect.close()
class QSBKSpider(object):
    def __init__(self):
        # 设置基本网址 基本网址为所有需要爬虫网址的公共部分
        self.base_url = 'https://www.qiushibaike.com/hot/page/'
        # 设置爬虫的用户标识
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }
        # 创建一个数据管理的实例化对象dataTool
        # 并使其成为QSBKSpider的属性
        self.dataTool = dataManager()
    def get_code_from_url(self,index):
        # 拼接完整的url路径
        url = self.base_url+str(index)+'/'
        # 设置请求的url和请求头信息
        request = Request(url,headers=self.headers)
        # 获取响应的信息
        response = urlopen(request)
        try:
            # 读取响应信息并解码
            code = response.read().decode()
        except Exception as e:
            print('获取信息失败',e)
        else:
            return code
    def get_user_info_from_code(self,code):
        pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<span class="stats-vote">.*?<i class="number">(.*?)</i>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S)
        # 获取所有抓取内容的总和
        result = pattern.findall(code)
        # oldData 为元组（姓名，年龄，内容，喜欢数，评论数）
        for oldData in result:
            # 更新旧值得到一个新值
            newData  = self.dataTool.update_new_data(oldData)
            # 将数据插入到数据库当中
            DBManager.insert_info_to_table(newData)
DBManager.create_db_and_table()
qbSpider = QSBKSpider()
for x in range(1,6):
    code = qbSpider.get_code_from_url(x)
    qbSpider.get_user_info_from_code(code)