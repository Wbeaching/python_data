
def text():
    pass
text()
def text(a):
    pass
text('a')
a=0
def text():
    global a
    a='XX'
    b=0
text()
print(a)
# print(b)
def text():
    return 1
print(text())
def text(a):
    return a+1
print(text(1))
def text(a,b=3):
    print(a+b)
text(3,5)
text(a=10,b=4)
# 默认参数必须放在列表的队尾
# 普通形参必须放在默认参数的前面
def textA():
    return 200
def textB(argument):
    print(argument)
textB(textA())
def text(a,*args):
    print(a)
    print(args)
text(1,2,3,4,5,6)
space = '----'
code = 'hello world'
print(space.join(code))
def text(content,insert):
    print(insert.join(content))
text('今天是周四，马上周六，好开心','!')
def newmap(value):
    print(value)
list(map(newmap,[1,2,3,4]))
def changalldata(value):
    return '完成时间：2018年8月8日'
result = list(map(changalldata,['学习音乐','学习绘画']))
print(result)
def changdata(value):
   print('2018年8月8日')
changdata('学习音乐')
changdata('学习绘画')
from functools import reduce
def newreduce(value1,value2):
    return value1+'的好朋友是'+value2+''
result = reduce(newreduce,['小王','小张','小美','小明'])
print(result)
def count(index1,index2):
    return index1+index2
result = reduce(count,[1,2,3,4,5])
print(result)
def text(a,*args,**kwargs):
    print(a)
    print(args)
    print(kwargs)
# kwargs必须是一个关键参数
text('张三',17,True,'李四',{'name':'王五'},friend = '赵六')
# 声明一个函数 可以进行任意加减乘除运算
def myfun(content,method = '+'):
    content = method.join(content)
    print(eval(content))
myfun('12334455','*')
# 匿名函数
result = lambda x:x
print(result(2))
def text(x):
    return x
print(text(2))
result = lambda x,y:x+y
print(result(5,6))
def test(x,y):
    return x+y








