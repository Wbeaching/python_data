
import re
from urllib.request import Request,urlopen
import sqlite3
# 专门处理各种数据 使其符合要求
class DataManager(object):
    # 该方法负责修改数据 取出不必要的内容
    def updata_new_data(self,oldData):        # print(oldData)
        name =oldData[0]
        name = name.strip('\n')
        content = oldData[2]
        content = content.strip('\n')
        pattern = re.compile(r'<br>')
        content = pattern.sub('',content)
        newData = (name,oldData[1],content,oldData[3],oldData[4])
        return newData
class DBManager(object):
    connect =None
    cursor = None
    @classmethod
    def create_db_and_table(cls):
        cls.connect = sqlite3.connect('qbDB')
        cls.cursor = cls.connect.cursor()
        cls.cursor.execute('create table if not exists qbTable(name text,age text,content text,like text,conment text)')
        cls.connect.commit()
    @classmethod
    def insert_info_to_table(cls,receiveData):
        cls.cursor.execute('insert into qbTable(name,age,content,like,conment) VALUES ("{}","{}","{}","{}","{}")'.format(receiveData[0],receiveData[1],receiveData[2],receiveData[3],receiveData[4]))
        cls.connect.commit()
    @classmethod
    def close_db(cls):
        cls.cursor.close()
        cls.connect.close()
class QSBKSpider(object):
    def __init__(self):
        # 设置基本网址 基本网址为所有爬虫的网址的共同部分
        self.base_url = 'http://www.qiushibaike.com/hot/page'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        # 创建一个数据管理的实例化对象dataTool
        # 并使其作为QBBKSpider的属性
        self.dataTool = DataManager()
    def get_code_from_url(self,index):
        # 拼接完整的url路径
        url = self.base_url+str(index)+'/'
        # 设置请求信息的url和请求路径
        request = Request(url,headers=self.headers)
         # 获取相应信息
        response = urlopen(request)
        try:
         # 读取相应信息并解码
             code = response.read().decode()
        except Exception as e:
             print('获取信息失败',e)
             return None
        else:
            return code
    def get_userfull_info_from_code(self,code):
        # print(code)
        patter = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<span class="stats-vote">.*?<i class="number">(.*?)</i>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S)
        result = patter.findall(code)
        # print(result)
        # result获取所有抓取的内容
        for oldData in result:
         # oldData为元组(姓名 年龄 内容，喜欢数 评论数）
         # 更新旧值得到新值
            newData=self.dataTool.updata_new_data(oldData)
            # 插入数据到数据库
            DBManager.insert_info_to_table(newData)
DBManager.create_db_and_table()
qpSpider = QSBKSpider()
# code=qpSpider.get_code_from_url(1)
for x in range(1,6):
    code = qpSpider.get_code_from_url(x)
    qpSpider.get_userfull_info_from_code(code)
DBManager.close_db()
