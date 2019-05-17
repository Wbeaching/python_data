
# 默认参数必须放在参数队尾后面
# 普通参数必须放在默认参数前面
# def text(b=3,a):
#     pass
def textA():
    return 20
def textB(argument):
    print(argument)
# 函数里面的参数可以是任意类型
textB(textA())
def text(a,*args):
    print(a)
    print(args)
text(1,2,3,4,5,6)















