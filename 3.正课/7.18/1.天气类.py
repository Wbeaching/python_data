#
# import sqlite3
# from urllib.request import urlopen
# from urllib.parse import quote
# import string
# import json
# from xpinyin import Pinyin
# p= Pinyin()
# class Weather(object):
#     def __init__(self,citylist = []):
#         self.citylist = citylist
#         self.connect = None
#         self.curosr = None
#
#     def getallinfo(self):
#         # 创建/打开数据库
#         self.openDB()
#         for city in self.citylist:
#             cityName = p.get_pinyin(city)
#             cityName = p.get_pinyin(city).replace('_','')
#             self.curosr.execute('create table if not exists"{}"(day text,heigh text,low text)'.format(cityName))
#             self.connect.commit()
#             url =
#
#
#     def getallinfo(self):...
#
#     def getinfowith(self,info):
#         # 郑州
#         # info ['city'] info['time']
#         info['city'] = p.get_pinyin(info['city']).replace('_','')
#         self.openDB()
#         self.curosr.execute('select*from "{}"WHERE day LIKE "%{}%"'
#                             .format(info['city'],info['time']))
#         self.connect.commit()
#         result = self.curosr.fetchall()
#         if result:
#             print(result)
#         else:
#             print('暂无徐相关信息')
#     def openDB(self):
#         self.connect = sqlite3.connect('weatherDB')
#         self.curosr = self.connect.cursor()
#     def closeDB(self):
#         self.connect.commit()
#         self.curosr.close()
#         self.connect.close()
#
# w = Weather(['郑州','洛阳','开封','南阳','商丘','驻马店','周口','平顶山'])
# w.getallinfo()
# dic = {}
# dic['city'] = input('你想查询哪个城市')
# dic['time'] = input('你想查询哪一天')
#
# class movie(object):
#     def __init__(self):
#         self.connect = None
#         self.curosr = None
#         self.url = ''
#     def getAllInfo(self):
#         self.connect = sqlite3.connect('movieDB')
#         self.curosr = self.connect.cursor()
#         uel = ''
#         response = urlopen(url)
#         responseStr = response.read()
#         responseDic = json.load(responseStr)
