# request 请求
# connect  连接
# manager  管理
# commit   提交
# close   关闭
# execute  执行
# compile  编译；汇编
# type    类型
# 在....内部  inside
# 在。。。。外部  outside
# open   打开
# match   匹配
# host  主机
# response  响应
# search  寻找
# load  加载
import re
from urllib.request import Request,urlopen
import sqlite3
# 目的：获取贴吧的内容，存储到数据库和txt
#     A.注意url规律
#     1.拼接url （拼接后第一页以后要获取一共多少页）
#     B.用不用代理IP User-Agent 注意源码内容
#     2.拼接后获取网页源码 code
#     C.注意源码中是否有该数据数据
#     3.存储到数据库
#     D.是否连接到数据库  光标是否初始化  数据库的格式
#     4.如果数据库属于楼主，则同时存储到txt
#     E.'w','a','r'
class DBManager(object):
    connect = sqlite3.connect('TieBa')
    cursor = connect.cursor()
    @classmethod
    def create_table(cls):
        cls.cursor.execute('create table if not exists TieBaTable(name txt content txt)')
        cls.connect.commit()
    @classmethod
    def inserte_into_table(cls,receiveData):
        cls.cursor.execute('insert into tiebaTable(name,content) VALUES ("{}","{}")'.format(receiveData(0),receiveData(1)))
        cls.connect.commit()
    @classmethod
    def close_Tieba(cls):
        cls.cursor.close()
        cls.connect.close()
class DataManger(object):
    def __init__(self):
        self.code = ''
    # 获取总页码数
    def get_total_page(self,code):
        # 注意：代码执行到这的时候self.code 已经被赋值
        self.code = code
        pattern = re.compile(r'<span class="red">(.*?)</span>',re.S)
        result = pattern.findall(code)[0]
        # 将result的值返回给 调用get_tobal_page方法的对象
        return result
    def get_name_and_content(self):
        pattern = re.compile(r'<a.*?class="p_author_name.*?".*?>(.*?)</a>.*?<div .*?class"d_post_content j_d_post_content".*?>(.*?)</div>',re.S)
        result = pattern.findall(self.code)
        print(result)
        space_content = re.compile(r'\s',re.S)
        italic_content = re.compile(r'\u3000',re.S)
        # 去除任意标签
        br_content = re.compile(r'<.*?>',re.S)
        for name,content in result:
            # 去除换行
            name = name.strip('\n')
            # 去除空格
            name = re.sub(space_content,'',name)
            name = re.sub(italic_content,'',name)
            name = re.sub(br_content,'',name)
            content = content.strip('\n')
            content = re.sub(space_content,'',content)
            content = re.sub(italic_content,'',content)
            content = re.sub(br_content,'',content)
            DBManager.inserte_into_table(name,content)
            # print(name)
            # print(content)
            if name =='恶人能活一世纪':
                with open('xs.txt','w',encoding='utf-8') as f :
                    f.write('{}'.format(content))
                f.close()

class tieBaSpider(object):
    def __init__(self):
        self.base_url = 'https://tieba.baidu.com/p/4685013359?pn='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        # 将数据管理作为自己个属性
        self.dataManager = DataManger()
        self.total_page = '1'
        self.current_page= 1
    def star_spider(self,pageIndex):
        url = self.base_url+str(pageIndex)
        request = Request(url,headers=self.headers)
        response = urlopen(request)
        result = response.read().decode()
        # 将所有的数据传给dataManager对象的get_total_page方法
        # 如果代码中要调用其他方法啊，那么先执行其他代码里的代码
        # 然后回到这里继续执行这里的代码
        self.total_page = self.dataManager.get_total_page(result)
        # 代码执行到这：获取源码，分离数据，存入数据路已完成
        self.dataManager.get_name_and_content()
        if self.current_page<int(self.total_page):
            self.current_page+=1
            self.star_spider(self.current_page)


DBManager.create_table()
tieBa = tieBaSpider()
tieBa.star_spider(1)
# DBManager.close_Tieba()

