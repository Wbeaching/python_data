

# beautiful 美丽的
# soup 汤
from bs4 import BeautifulSoup
# beautifulsoup是python的一个第三库
# 和xpath作用一样，都是用来解析数据的
# 相比之下，xpath的速度快
# xpath的底层是用c来实现的

# beautifulsoup 里面需要两个参数
# 一个open方法，一个固定写法lxml
# open里面两个参数
# 1.想要解析数据
# 2.设置编码格式
bs = BeautifulSoup(open('2.add.html',encoding='utf-8'),'html')
print(bs)
print(type(bs))
# 获取网页当中的title标签
print(bs.title)
# 获取head标签及标签内部其他的标签
print(bs.head)
# 获取网页中的第一个a标签
print(bs.a)
# 总结：bs.XX
# 获取所有XX当中的第一个XX以及第一个XX里面的内容
# document 文档
# name再次指的是获取当前内容的标签名 bs为一个整体，而不是一个具体的标签
print(bs.name)
# 获取head的标签名
print(bs.head.name)
# 获取title的标签名
print(bs.title.name)
# attr
# attribute 属性
# 获取指定标签的所有属性
# 如果没有做特别处理，bs.XX 永远获取的所有XX中的第一个XX
print(bs.a.attrs)
# KeyError 只能从自己有的属性中找
print(bs.a['id'])
print(bs.a['href'])
# class 和 id不一样
# id 必须是唯一的 ，一个标签只能有一个id
# class 不是唯一的，不同标签可以拥有同一个class
# 同一标签也可以拥有多个class
print(bs.a['class'])
print(bs.html['lang'])
# del delete  删除
del bs.a['id']
print(bs.a)
# 获取指定标签的文本内容
print(bs.a.string)
# string 指的是本标签的文本，不包含子标签的文本
print(bs.div.string)
# 遍历------------------------
# contents 能够获取指定标签下面的所有内容
print(bs.head.contends)
print(bs.body.contents)
# 获取所有内容当中指定索引的内容
print(bs.div.contents[3])
# parent 父级
# 获取指定标签的父级标签和父级标签的所有标签
head = bs.title.parent
print(head)
print(type(head))
res = bs.find_all('a')
print(res)
for value in res:
    print(value)
# id是唯一的 通过id来找 只能找到一个 所以用find
# class 不是唯一的 通过class来找 可能找到很多
print(bs.find(id="jd"))
print(bs.find_all(class_='shopping'))
# 找到所有符合的第一个class
print(bs.find(class_='shopping'))
print(bs.find_all(id='jd'))

# select 选择
# 选择指定的标签
print(bs.select('title'))
# 当选择对象有多个的时候，将获取所有对象
print(bs.select('a'))
 # . 表示类名  #表示id
print(bs.select('.first'))
print(bs.select('#jd'))
# print(bs.select('href'))
# 找到一个类名为now的div标签
print(bs.select('div.now'))
