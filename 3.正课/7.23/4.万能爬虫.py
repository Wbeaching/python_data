from urllib.request import Request,urlopen
import re
import sqlite3
class DBManager(object):
    connect = sqlite3.connect('okDB')
    cursor = connect.cursor()
    isoneInfo =True
    # dbData = None
    @classmethod
    def create_table(cls,info):
        if DBManager.isoneInfo==True:
            cls.cursor.execute('create table if not exists spiderTable(value0 text)')
            cls.connect.commit()
        else:
            sqlstr = 'create table if not exists spiderTable('
            for index ,value in enumerate (info):
                # 'create table if not exists spiderTable(value0 text ,value1 text ,value2 text)'
                sqlstr +=  'value'+str(index)+' text,'
            sqlstr = sqlstr[0:-1]
            sqlstr += ')'
            cls.cursor.execute(sqlstr)
            cls.connect.commit()
            # print(sqlstr)
    @classmethod
    def insert_into(cls,info):
        if DBManager.isoneInfo==True:
            cls.cursor.execute('insert into spiderTable(value0) VALUES ("{}")'.format(info))
            cls.connect.commit()
        else:
            # 'insert into spiderTable(value0 ,value1,value2) VALUES (1,2,3)'
            key = ''
            values = 'values('
            sqlStr = 'insert into spiderTable('
            for index ,value in enumerate(info):
                key += 'value'+str(index)+','
                values+= '"' +info[index]+ '"' + ','
            key = key[0:-1]
            key += ')'
            values = values[0:-1]
            values+=')'
            sqlStr += key+values
            cls.cursor.execute(sqlStr)
            cls.connect.commit()
            # print(key)
            # print(value)
            # print(info)
            print(sqlStr+key+values)
class DataManager(object):
    # 根据源码获取指定的内容
    @classmethod
    def get_info_with_code(cls,code,patternValue):
        pattern = re.compile(r'{}'.format(patternValue),re.S)
        result = pattern.findall(code)
        # print(result)
            # 如果获取的是一条数据，那么这条数据类型是字符串，会被放入到列表中
            # 如果获取的是多条数据，那么每条数据都是元祖，也会被放入到列表中
            # if result[0]=='str':
            #     for value in result:
            #         value = value.strip('\n')
            #         print(value)
            # else:
        return result
    @classmethod
    def change_data_with(cls,olddata):
        space = re.compile(r'\s', re.S)
        element = re.compile(r'<.*?>', re.S)
        if type(olddata)==str:
            olddata = olddata.strip('\n')
            olddata = re.sub(space, '', olddata)
            olddata = re.sub(element, '', olddata)
            DBManager.isoneInfo =True
            return olddata
        else:
            list = []
            for content in olddata:
                content = content.strip('\n')
                content = re.sub(space,'',content)
                content = re.sub(element,'',content)
                list.append(content)
                DBManager.isoneInfo=False
            return list
class Spider(object):
    def __init__(self,base_url,pattern):
        self.base_url= base_url
        self.pattern = pattern
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    def load_url(self):
        url = self.base_url+'1'
        request = Request(url,headers=self.headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('请求页错误',e)
        else:
            # print(code)
             result_list=DataManager.get_info_with_code(code,self.pattern)
             for value in result_list:
                 # 字符串  列表
                 newData=DataManager.change_data_with(value)
                 # 创建数据表
                 DBManager.create_table(newData)
                 DBManager.insert_into(newData)
spider = Spider('http://www.qiushibaike.com/hot/page/','<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>')
spider.load_url()















