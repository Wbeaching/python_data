def test():
    pass
test()
def test(a):
    pass
test('a')
a=0

def test():
    global a, b
    a = "xxx"
    b = "999"
test()
print(a)
print(b)
def test():
    return 1
print(test())
def test(a):
    return a+1
print(test(1))
def test(a,b=3):
    print(a+b)
test(2,4)
test(a=8,b=9)
# 默认参数必须放在队尾
# 普通参数必须放在默认参数的前面
# def test(b=3,a):
#     pass
# test()
def testA():
    return 200
def testB(argument):
    print(argument)
    # 函数里面可以为任意类型
testB(testA())
def test(a,*args):
    print(a)
    print(args)
test(1,2,3,4,5)
print('----------------------------')
space='----'
code = 'Hello World'
print(space.join(code))
def test(content,insert):
    print(insert.join(content))
test("今天是周四，马上周六了，好开心","！")
# map reduce
# map里面必须穿两个值
# 值1：必须是函数
# 值2：必须是序列/容器
# 将序列里面的每个元素单独放入函数中执行
def newMap(value):
    print(value)
list(map(newMap,[1,2,3,4]))
# 需求：将数据表里面所有的数据前面添加一个完成的时间
# map 的作用就是依次处理序列里面的所有程序
# 和for循环非常类似
def change_all_data(value):
    return "完成时间:2018-8-8"+value
result = list(map(change_all_data,['学习数学','学习语文',"学习化学"]))
print(result)
def changeData(value):
    pass
# changeData('学习数学')
# changeData('学习语文')
from functools import reduce
def newReduace(value1,value2):
    # reduce 会将里面的所有元素操作两次
    # 实现步骤是
    # 将任意一个值前面的两个值进行处理
    # 处理的结果再给这个值进行处理
    # 处理的结果给下一个值使用
    # 所以必须有返回值
    return value1+'的好友是'+value2+','
result = reduce(newReduace,['小王','小张','小美','小红'])
print(result)
def count(index1,index2):
    return index1+index2
result = reduce(count,[1,2,3,4,5,6,7])
print(result)
def test(a,*args,**kwargs):
    print(a)
    print(args)
    print(kwargs)
test('张三',17,True,'李四',{'name':'王五'},"hello world",frieng='赵六' )
content ='print("hello world")'
print(content)
# 将指定的字符串当作代码处理
eval(content)
print('------------------')
# 声明一个函数 可以进行任意的加减乘除运算
def myFun(content,method='+'):
    content = method.join(content)
    print(eval(content))
myFun('1223344','+')
# 没有名字的函数叫匿名函数
def test():
    pass
test()
# lambda 表示该函数为匿名函数
# 匿名函数后面的x表示接受的参数
#  ":x" 表示返回x的值
result = lambda x:x
print(result(2))
def test(x):
    return x
print(test(5))
result = lambda x,y:x+y
print(result(3,5))
def test(x,y):
    return x+y
print(test(3,5))
list = [23,45,622,6763,13,3,5,677,24,7,87]
list = sorted(list,key = lambda x:x, reverse =True )
print(list)
import random
str = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
# def getRandom():
#     with open('random.txt','w') as f:
#         for index in range(1000):
#             content = ''
#             for x in range(10):
#                 char = random.choice(str)
#                 content+=char
#             f.write(content+'\n')
#     f.close()
# getRandom()
# 读取文件所有的数据
def readAllInfo():
    list = []
    with open('random.txt','r') as f:
        for line in f.readlines():
            line = line[0:-1]
            list.append(line)
    f.close()
    return list
readAllInfo()
print('----------------------------')
# 获取所有的数据中都为数字的数据
def getAllNuminfo():
    list = readAllInfo()
    with open('num.txt','w') as f :
        for value in list:
            if value.isdigit():
                f.write(value+'\n')
    f.close()
getAllNuminfo()
# 获取所有是字母的数据
def getAllCharInfo():
    with open('char.txt','w') as f:
        list = readAllInfo()
        for x in list:
            if x.isalpha():
                f.write(x+'\n')
    f.close()
getAllCharInfo()
def getAllNumAndCharInfo():
    list = readAllInfo()
    with open('numandchar.txt','w')as f:
        for value in list:
            isHasChar = False
            isHasNum = False
            for char in value:
                if char.isdigit():
                    isHasNum =True
                else:
                    isHasChar = True
            if isHasChar == True and isHasNum == True:
                f.write(value+'\n')
    f.close()
getAllNumAndCharInfo()