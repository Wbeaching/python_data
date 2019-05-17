
import os
# os可以获取本机的基本信息以及
# 可以对文件夹及文件进行操作
# nt代表windows操作系统
# posix 代表linux操作系统
name = os.name
print(name)
cpu_count = os.cpu_count()
# 获取cpu核数
print(cpu_count)
# 判断是否存在某个文件
# path 路径 exists存在
# 如果不写路径地址，直接写文件名字
# 那么默认使用得是 相对路径
result = os.path.exists('测试.txt')
print(result)
# 绝对路径
result = os.path.exists('C:/Users/Administrator/Desktop/python资料/3.正课/7.11/测试.txt')
print(result)
# 获取绝对路径
result = os.getcwd()
print(result)
# abs absolute 绝对的
result = os.path.abspath('.')
print(result)
# 获取当前路径的父路径
result = os.path.abspath('..')
print(result)
# 获取整个地址当中的最后一部分
result = os.path.basename('http://www.baidu.com/music/prettyboy.mp3')
print(result)
result = os.path.basename('C:/Users/Administrator/Desktop/python资料/3.正课/7.11/3.os.操作.py')
print(result)
# 地址路径会被分割成几部分
result = os.path.commonpath(['http://www.jd.com',
                             'http://taobao.com',
                             'http://baidu.com'])
print(result)
# 返回文件所在的文件夹
# 文档：返回一个文件夹的共有路径
result= os.path.dirname('C:/Users/Administrator/Desktop/python资料/3.正课/7.11/3.os.操作.py')
print(result)
# --------------文件夹信息处理--------
import time
# gec得到  c chang/creat
# 获取文件夹的创建时间
result = os.path.getctime('C:/Users/Administrator/Desktop/python资料/3.正课/7.11/3.os.操作.py')
print()
print(time.localtime(result))
# 访问时间 # a access 访问时间
result = os.path.getatime('C:/Users/Administrator/Desktop/python资料/3.正课/7.11/3.os.操作.py')
print(time.localtime(result))
# modify 修改
result = os.path.getmtime('C:/Users/Administrator/Desktop/python资料/3.正课/7.11/3.os.操作.py')
print(time.localtime(result))
# getsize获取文件的大小 获取的为字节大小
result = os.path.getsize('C:/Users/Administrator/Desktop/python资料/3.正课/7.11/3.os.操作.py')
print(result/1024)
# is 是否
result = os.path.isfile('C:/Users/Administrator/Desktop/python资料/3.正课/7.11/3.os.操作.py')
print(result)
#
# 返回一个元组  由路径和最后的文件名字组成
result = os.path.split('C:/Users/Administrator/Desktop/python资料/3.正课/7.11/3.os.操作.py')
print(result)
# 返回一个元组 由全部的路径和最后的文件后缀组成
result = os.path.splitext('C:/Users/Administrator/Desktop/python资料/3.正课/7.11/3.os.操作.py')
print(result)
if os.path.exists('python'):
    pass
else:
    os.mkdir('python')
if os.path.exists('测试.txt'):
    os.rename('测试.txt','发布.txt')
# 文件读写------------
# 值1：写入的文件，如果有这个文件就直接写入，没有这个文件就创建
# 值2：对文件操作的方式，w 表示 write 写
# 值3：文件的编码方式，utf-8方式乱码出现
f= open('python.txt','w',encoding='utf-8')
f.write('今天是周三，7月11日，距离毕业还有120天\n')
# 当文件关闭以后 不能对文件进行任何操作
f.write('明天是周四，后天是周五，大后天自习，然后就休息\n')
f.close()
f = open('python.txt','a',encoding='utf-8')
f.write('新内容---------')
f.close()
f = open('python.txt','r',encoding='utf-8')
# f.readlines 将所有的数据放入到一个数组当中
# f.read 将所有的数据放入到一个字符串当中
result = f.read()
print(result)
f.close()
import random
f= open('code.txt','w',encoding='utf-8')
for x in range(10000):
    content = ''
    for y in range(6):
        num = random.randint(0,9)
        content += str(num)
    f.write(content+'\n')
f.close()