import sqlite3
import random
connect = sqlite3.connect('nameDB')
curosr = connect.cursor()
curosr.execute('create table if not exists nameTable(name text)')
connect.commit()
str = """
赵钱孙李，周吴郑王。
冯陈褚卫，蒋沈韩杨。
朱秦尤许，何吕施张。
孔曹严华，金魏陶姜。
戚谢邹喻，柏水窦章。
云苏潘葛，奚范彭郎。
鲁韦昌马，苗凤花方。
俞任袁柳，酆鲍史唐。
费廉岑薛，雷贺倪汤。
一二三四，东西南北
"""
str = str.replace('，','').replace('。','').replace('\n','')
print(str)
for x in range(1000):
    name = ''
    for y in range(random.randint(2,3)):
        char = random.choice(str)
        name += char
    # print(name)
curosr.execute('INSERT INTO nameTable (name) VALUES ("{}")'.format(name))
connect.commit()
def get_all_match_info():
    # like 是数据库进行匹配的关键字 后面为匹配的规则
    # x_表示找到以x为开头，后面只有一位的数据
    # __多少位 就表示找到后面有几位的数据
    curosr.execute('SELECT *FROM  nameTable WHERE name LIKE "张_"')
    # print(curosr.fetchall())
    curosr.execute('SELECT *FROM nameTable WHERE name LIKE "_王"')
    # print(curosr.fetchall())
    # %x 表示找到以x结束的数据
    curosr.execute('SELECT *FROM nameTable WHERE name LIKE "%李"')
    # print(curosr.fetchall())
    # x% 表示找到以x开始的数据
    curosr.execute('SELECT *FROM nameTable WHERE name LIKE "冯%"')
    # print(curosr.fetchall())
    # %x% 表示所有包含x的数据
    curosr.execute('SELECT *FROM nameTable WHERE name LIKE "%花%"')
    print(curosr.fetchall())
    # print(curosr.fetchall())
get_all_match_info()