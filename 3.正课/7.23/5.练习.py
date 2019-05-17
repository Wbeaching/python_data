from urllib.request import Request,urlopen
import re
import sqlite3


class DBManager(object):
    connect= sqlite3.connect('AAA')
    cursor = connect.cursor()
    isOneInfo = True
class dataManager(object):
    @classmethod
    def get_data_with_code(cls,code,patternvalue):
        pattern = re.compile(r'{}'.format(patternvalue),re.S)
        result = pattern.findall(code)
        print(result)
        return result
    @classmethod
    def change_deta(cls,olddata):
        space = re.compile(r'\s',re.S)
        element = re.compile(r'<.*?>',re.S)
        if type(olddata)==str:
            olddata = olddata.strip('\n')
            olddata = re.sub(space,'',olddata)
            olddata = re.sub(element,'',olddata)
            print(olddata)
        else:
            list = []
            for content in olddata:
                content = content.strip('\n')
                content = re.sub(space,'',content)
                content = re.sub(element,'',content)
                list.append(content)
            print( list)



class TieBaSpite(object):
    def __init__(self,base_url,pattern):
        self.base_url = base_url
        self.pattern = pattern
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
        }
    def full_url(self):
        url = self.base_url+'1'
        request = Request(url,headers=self.headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('没找到',e)
        else:
            # print(code)
            result_list=dataManager.get_data_with_code(code,self.pattern)
            for value in result_list:
                print(type(value))
                # dataManager.change_deta(value)
url = TieBaSpite('http://www.qiushibaike.com/hot/page/','<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>')
url.full_url()