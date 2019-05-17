
# 异常处理：提前先将可能会引起错误的代码
# 放入到捕获异常代码块当中，一旦
# 发生错误，不会影响后续代码的执行

try:
    list = [1, 2, 3, 4, 5, 6]
    print(list[100])
    dic = {'name': '张三'}
    print(dic['age'])
except KeyError as e:
    print('捕获了一个key值错误，请仔细检查')
except IndexError as e:
    print('捕获了一个索引值错误，索引值超出界限')

try:
    list = [1,2,3,4]
    print(list[100])
    dic = {'name':'Vik'}
    print(dic['age'])
# 捕获任意错误 好处是不需要遍历所有错误
# 缺点：不知道错误类型
except Exception as e:
    print('捕获一个错误')
# 有可能错误的代码块
try:
    list = [1,2,3]
# 捕获了错误的代码块
except Exception as e:
    print('捕获了一个错误')
# 代码没有产生错误的代码块
else:
    print('没有错误')
# 不管有没有没有错误 一定会进来的代码块  finally最终的
finally:
    print('程序结束')