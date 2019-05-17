# return 和 yield的区别
# return可以往返方法外传递一个值，之后return后面的代码统统不执行
# yield 可以往方法外面传递一个值，但是传递以后，继续回到yield后面开始执行
# 通过yield传递的值是一个可迭代的对象
def test1(name):
    print('return方法')
    return name
    print('return方法结束')
name = test1('张三')
print(name)

def test2(name):
    print('yield方法')
    yield name
    print('yield方法结束')
name = test2('lisi')
print(name)
def test2(age):
    for i in range(age):
        yield i
        print('hello')
for x in test2(18):
    print('x=',x)