
str =''
str = ""
str =''''''
str = """"""
""""
python里面的多行注释 用这种方式
其实质 就是一个大字符串
"""""
# 字符串 ：一串字符连接在一起，称之为字符串
# 字符：
# 在有基本类型数据的其他语言里：char声明的是字符 string声明的字符串
# char
# string
#在引号里面写的内容 不管是什么 都是字符串
content = ''
content = 'hello world'
#------------------------------字符串切片操作-----------
#字符串也是一个容器 可以存放任意字符
# 容器里面的所有元素都有一个编号
# 编号从0开始
print(content[0])
# print(content[21])
#指定索引获取开始到结束的内容
print(content[3:])
#获取字符串到指定索引的内容（不包括指定索引的位置）
print(content[:3])
print(content[3:6])
#  : 前面是开始位置 如果不写 默认为0
#  : 后面为结束位置 如果不写 默认到结尾
print(content[:-1])
print(content[1:-1])
#颠倒字符串里面的内容
print(content[::-1])
#值1：从哪开始
#值2：到哪结束
#值3：每次往后隔几位  默认是1
print(content[1::2])
#以上操作都没有改变字符串的内容
#如果要改变 需要这样写
content = content[1:4]
print(content)
# ---------------find-------------------
content = 'hello world'
#查看content里面有没有指定的字符串
#如果返回-1 则表示没有找到指定内容
#如果返回其他值 表示找到 返回的值为字符在字符串的当中的索引
#英文大小写字母在ASCII代表的意义不同
print('----------')
result = content.find('l')
print(result)
#作业：不能使用find方法，自己模拟find方法的实现过程
#判断字符串中有没有包含指定字符，如果有，返回其
# 在字符串中的位置，如果没有返回-1
#--------------index -------------
# content = 'hello world'
# # ValueError: substring not found
# # 值错误：字符串未找到
# result = content.index('你好')
# print(result)
#-------------count----------
content = 'hello world'
#获取指定字符在字符串当中的个数
result = content.count('e')
print(result)
#----------------replace---------
content = 'hello world'
result = content.replace('l','t')
print(result)
#-------------split---------
content = 'hello world'
result = content.split('l')
print(result)
#------------大小写转换----------
content = 'hello WORLD'
#字符全部小写 只能转化成英文字母大小写
print(content.lower())
#字母全部大写
print(content.upper())
#首字母大写，其余小写
print(content.capitalize())
#转化成小写 支持utf-8中文字符大小写
print(content.casefold())
#------------start ,end---------
content = 'Hello World'
print(content.startswith('w'))
print(content.endswith('d'))
#--------------maketrans-----------
content = '习近平近日来智游某基地进行参观并做了重要讲话'
s = str.maketrans('智游','XX')
#让content 遵守规则
content = content.translate(s)
print(content)



























