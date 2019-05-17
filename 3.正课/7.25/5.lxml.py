

import requests
import re
from lxml import etree


url = 'http://www.qiushibaike.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
response = requests.get(url,headers = headers).content
print(response)
# re.compile(r'<div class="author clearfix">.*?<h2>(.*?)')
# 将字符串转化成html代码
root = etree.HTML(response)
# element 元素；节点 ；标签
print(root)
# 从根标签开始找 找到类名为author clearfix 的标签
# a 找到某一个标签下面的a 标签
# text（） 获取标签的文本
name_list = root.xpath('//div[@class="author clearfix"]/a/h2/text()')
print(name_list)
content_list = root.xpath('//div[@class="content"]/span/text()')
print(content_list)


# 美食杰 使用cookie 模拟登陆 获取网页源码 使用xpatn 得到用户信息 存储到Excel表格




