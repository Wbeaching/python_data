# 定义一个爬虫类 需要两个参数  1个是url地址 一个是正则表达式，根据两个参数将获取的内容写入到本地数据库
# 将正则表达式获取的内容写入到数据库
# 确保在代码不修改的情况下 至少 能爬虫五个网页
# jd  taobao 百度 mi huawei
# 要求：每人必写
import re
from urllib.request import Request,urlopen
import sqlite3
class WZSpider(object):
    def __init__(self):
        self.base_url = 'http://www.'
        self.headers ={
            'User-Agent':' Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
        }
    def get_full_url(self,index):
        url = self.base_url+index
        request = Request(url,headers=self.headers)
        response = urlopen(request)
        code = response.read().decode()
        return code
    def get_all_info_from_code(self,code):
        pattern = re.compile(r'')
        result = pattern.findall(code)
        print(result)
wz = WZSpider()
code=wz.get_full_url('baidu.com')
wz.get_all_info_from_code(code)