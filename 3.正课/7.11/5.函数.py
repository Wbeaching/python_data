

# 函数就是方法类似于生活中的模具/模板
# 声明方法 def define 定义 test 方法名称 （）内部写参数
def test():
    pass
test()
# 无参数无返回值
def firstFun():
    print('this is my first function')
firstFun()
# 有参数无返回值  声明方法的时候的参数叫做形式参数，简称形参
# 形参没有具体的指 ，本身没有一个变量
def secondFun(values):
    print('我喜欢'+values)
secondFun('学习')
 # 调用方法时候的参数 叫实际参数 简称实参
# 实际不是变量 而是具体值
secondFun('1,2,3')
# 局部变量和全局变量
# 在方法内部的声明的变量叫局部变量
# 只能在方法内部使用
# 出来方法就释放了

# 无参数有返回值
def thirdFun():
    love = 'ai 学习'
    return love
result = thirdFun()
print(result)
def fourFun():
    print('hello')
    return
    # return 后面没有跟值的话，默认返回None
    # return 只能写在方法里面，不能在方法外面使用
    # 代码执行return以后 return 到方法结束之前
    # 的部分 统统不执行
    print('world')
fourFun()
# 有参数有返回值
def fiveFun(a,b):
    return a+b
fiveFun(12,13)
print(fiveFun(12,13))
# 有多参无返回值
def sixFun(a,b,c,d,e,f):
    print(a)
    print(b)
    print(c)
sixFun('a',0,[1,2,3,4,5,6,7],True,{'name':'张三'},(1,2,3))
# 默认参数
def myGirfriend(name,age,sex =True,born ='未知'):
    print('我的女朋友{}，年龄是{}，性别是{}，出生日期是{}'.format(name ,age ,sex,born))
myGirfriend('小玲',100)
myGirfriend('小王',100,True,'1918年')
myGirfriend('小黄',100,True)
# 关键参数
def myBoyfriend(name,age,sex =False,born ='未知'):
    print('我的男朋友{}，年龄是{}，性别是{}，出生日期是{}'.format(name, age, sex, born))
myBoyfriend('小张',100)
# 指明给哪一个参数设置值，这种参数叫做关键参数
myBoyfriend('小张',100,born ='2000年1月1日')

# *args参数
# argument 参数**XXX
# *args 能够将多余的参数 统统放入到自己内部
def myArgu(name,*args):
    print(name)
    print(type(args))
    print(args)
myArgu('张三丰','149','武当创始人','太极剑','太极拳')









