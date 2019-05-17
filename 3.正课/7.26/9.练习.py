from lxml import etree
# element 元素;标签
# etree 标签树
html_str = """"""

html = etree.fromstring(html_str)
print(html)
print(type(html))
# 找到网页内所有a标签
a= html.xpath('//a')
# 获取指定标签的类名
result = html.xpath('//a@class')
# 获取所有a标签的id
result = html.xpath('//a@id')
# 获取指定标签的超链接属性
result = html.xpath('//a@href')
# 找到指定的文本内容
result = html.xpath('//a/text()')
# 只获取本标签的文本，子标签文本的内容不获取
result = html.xpath('//div/text()')
# 既获取本标签的文本，也获取子标签的文本
result = html.xpath('//div//text()')
# 获取指定标签的id标签文件
result = html.xpath('//ul/li/a[@id="jd"]/text()')
# last() 获取最后一个标签
result = html.xpath('//ul/li[last()]')[0]
# 获取拥有指定类名的标签文本
result = html.xpath('//a[@class="shopping"]/text()')
# contains 包含指定属性
result = html.xpath('//div[@class="now"]/p[contains(@class,"third")]/text()')
