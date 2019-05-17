from lxml import etree
# e element 元素；节点
# tree 树
#   标签树
html_str ="""
<a href="http://www.baidu.com">
    百度一下，你就知道
</a>
"""
# 将字符串转化为a标签
# 该方法会检测字符串内容是否为标签样式
# 但不能检测内容是否为真标签
result = etree.fromstring(html_str)
print(result)
# <Element a at 0x2235030>
# 0x2235030里面有一个a标签
# parse 解析
html = etree.HTML('2.add.html')
print(type(html))
print(html)
# 找到网页内所有的a标签

a = html.xpath('//a')
print(a)
# 获取指定标签的类名
result = html.xpath('//a@class')
print(result)
# 找到所有a标签的id
result  = html.xpath('//a@id')
print(result)
# 找到指定标签的超链接属性
result = html.spath('//a@href')
print(result)
# 找到指定的文本内容
result = html.xpath('//a/text()')
print(result)
# /text() 只获取本标签的文本，子标签文本不获取
result = html.xpath('//div/text()')
print(result)
# //text()找到本标签文本以及所有子标签的文本
result = html.xpath('//div//text()')
print()
# 获取指定id的标签文本
result = html.xpath('//ul/li/a[@id="jd"]/text()')
print(result[0])
# last()获取最后一个标签
result = html.xpath('//ul/li[last()]')[0]
print(result)
# 获取拥有指定类名的标签文本
result= html.xpath('//a[@class="shopping"]/text()')
print(result)
# contains 包含指定属性
result = html.xpath('//div[@class="now"]/p[contains(@class,"third")]/text()')
print(result)
# 第一// 找到所有的ul
# 第二// 找到所有ul标签中的a标签
# 获取a标签文本和所有a标签问的子标签文本
result = html.xpath('//ul//a//text()')
print(result)