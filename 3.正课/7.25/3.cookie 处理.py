


# CookieJary 有一些子类，分别是FileCookieJar ,LWPCookieJar,MoziliaCooieJar
# CookieJar 管理http生成的cookie 负责cookie 的存储工作，向http当中添加指定的cookie
from http.cookiejar import CookieJar,LWPCookieJar
from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener
from urllib.parse import urlencode
# 生成一个管理cookie的对象
"""
cookie_obj = CookieJar()
# 创建一个支持cookie的对象，对象属于HTTPCookiePrecessor
cookie_handler = HTTPCookieProcessor(cookie_obj)
# build_opener 内部的实现就是urlopen
# urlopen 只能进行简单的请求，不支持在线验证，cookie ,代理IP等复杂操作
opener = build_opener(cookie_handler)  # urlopen
response = opener.open('http://www.neihanshequ.com')
# print(response)
for cookie in cookie_obj:
    # print('key:',cookie.name)
    print('value:',cookie.value)


# 保存cookie------------------
filename = 'neihan.txt'
# 设置cookie 保存文件
cookie_obj = LWPCookieJar(filename=filename)
cookie_handler = HTTPCookieProcessor(cookie_obj)
opener = build_opener(cookie_handler)
response = opener.open('http://neihanshequ.com')
# 保存cookie到指定的文件中区
# ignore 忽略
# ignore_expires=即便目标cookie已经在文件中存在，仍然对其写入
# ignore_discard=True 即便cookie已经过期 ，仍然将其写入
cookie_obj.save(ignore_expires=True,ignore_discard=True)

# 使用本地cookie进行请求
cookie = LWPCookieJar()
cookie.load('neihan.txt')
request = Request('http://neihanshequ.com')
cookie_handler = HTTPCookieProcessor(cookie)
opener = build_opener(cookie_handler)
response = opener.open(request)
print(response.read().decode())


# 模拟登陆美食杰------------

cookie = LWPCookieJar(filename='meishi.txt')
cookie_handler = HTTPCookieProcessor(cookie)
opener = build_opener(cookie_handler)
hedaers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
post_url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fi.meishi.cc%2Flogin.php%3Fac%3Dzhuce'
# urlencode 对url中的参数进行编码
# quote 对url中的中文进行编码
# urlencode()编码的对象为字典
# quote 编码的对象为字符串
post_data = urlencode({
    'username':'2963079730@qq.com',
    'password':'199606184810zuo'
})
request = Request(post_url,bytes(post_data,encoding='utf-8'))
response = opener.open(request)
print(response.read().decode())
cookie.save(ignore_discard=True,ignore_expires=True)
"""
# 利用登陆获取的cookie来请求美食杰首页
cookie = LWPCookieJar()
cookie.load ('meishi.txt',ignore_expires=True,ignore_discard=True)
opener = build_opener(HTTPCookieProcessor(cookie))
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
request = Request('http://www.meishijie.com')
response = opener.open(request)
print(response.read().decode())
