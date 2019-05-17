
space = '-----'
code = 'Hello World'
print(space.join(code))

def text(content,insert):

   print(insert.join(content))
text('今天是周四，马上周六，好开心','!')

# map reduce-----------------
def newMap(value):
   print(value)
# map 里面需要两个值
# 值1：必须是函数
# 值2：序列/容器
# 作用：将序列中的每个元素单独放入函数中执行
# list(map())
list(map(newMap,[1,2,3,4]))

# map 的作用依次处理序列里面的所有元素
# 和for循环相似
# 需求：将数据表里的所有数据前面添加一个完成时间
def changeAllData(value):
   return '完成的时间：2018-8-8'+value
result = list(map(changeAllData,['学习a','学习b','学习c']))
print(result)

from functools import reduce
def newReduce(value1,value2):
    # reduce 将序列里面的元素操作两次
    # 实现步骤：
    # 将任意一个值前面的两个值进行处理
    # 处理的结果给下一个值使用
    # 所以必须有返回值
    return value1+'的好朋友'+value2
result = reduce(newReduce,['小王','小张','小美','小明'])
print(result)
def count(index1,index2):
    return index1+index2
result = reduce(count,[1,2,3,4,5])
print(result)

def text(a,*args,**kwargs):
    print(a)
    print(args)
    # kwargs必须是一个关键参数，不能是字典类型
    # key = value  name ='张三' age = 17
    print(kwargs)
    # 方法里面的实参 必须和形参对应
text('张三',17,True,'李四',friend = '王五')
content = 'print("hello world")'
print(content)
# 将指定的字符串当代码处理
content = eval(content)
# 声明一个函数 可以进行任意的加减乘除运算
def myFun(content,method='+'):
    content = method.join(content)
    print(eval(content))
myFun('12823848','*')

# 匿名函数
# 函数都有名字的 没有名字的函数叫匿名函数
def text():
    pass
text()
# lambda 拜师该函数为匿名函数
# 匿名函数后面的x表示接收函数
result = lambda x:x
print(result(2))
def text(x):
    return x
print(result(2))
result = lambda x,y:x+y
print(result(3,4))
def text(x,y):
    return x+y
print(text(3,5))
list = [134,45,67,8,5543]
# sorted 排序   reverse=True反序
list = sorted(list,key = lambda x:x,reverse = True)
print(list)

# 声明方法1：
# 创建一个txt文件，里面存放1000条数据，每条数据长度为10 包含的小写字母和数字
# 声明方法2：
# 读取txt文件里面的所有数据，如果该条数据只有数字，那么创建一个txt文件，保存起来
# 声明方法3：
# 读取txt文件里面的所有数据，如果该条数据只有字母，那么创建一个txt文件，保存起来
# 声明方法4：
# 读取txt文件里面的所有数据，如果该条数据包含数字和字母，那么创建一个txt文件，保存起来