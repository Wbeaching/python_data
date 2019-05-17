

# 美食杰 使用cookie 模拟登陆 获取网页源码 使用xpatn 得到用户信息 存储到Excel表格
from http.cookiejar import CookieJar,LWPCookieJar
from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener
from urllib.parse import urlencode
from lxml import etree
import requests
# class MSSpider(object):
#     def __init__(self):
#         self.post_url
cookie = LWPCookieJar(filename='meishi.txt')
cookie_hadeler = HTTPCookieProcessor(cookie)
opener = build_opener(cookie_hadeler)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
post_url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fi.meishi.cc%2Flogin.php%3Fac%3Dzhuce'
post_data = urlencode({
    'username':'2963079730@qq.com',
    'password':'199606184810zuo'
})
request = Request(post_url,bytes(post_data,encoding='utf-8'))
response = opener.open(request)
# print(response.read().decode())
cookie.save(ignore_discard=True,ignore_expires=True)


cookie = LWPCookieJar()
cookie.load('meishi.txt',ignore_expires=True,ignore_discard=True)
opener = build_opener(HTTPCookieProcessor(cookie))
headers = {
    'USer-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
request = Request('https://www.meishij.net/')
response = opener.open(request)
# print(response.read().decode())
url = 'http://www.meishij.net'
headers = {
    'USer-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
response = requests.post(url,headers=headers)
root = etree.HTML(response.content)
User = root.xpath('//div[@class="bbtitles"]/div/text()')
print(User)
name_list = root.xpath('//div[@class="c1"]/em/text()')
# print(name_list)

