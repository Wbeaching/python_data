from http.cookiejar import CookieJar,LWPCookieJar
from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener
from urllib.parse import urlencode
# 生成一个管理cookie的对象
cookie_obj=CookieJar()
# 创建一个支持cookie的对象，对象属于HTTPCookiePrecssor
cookie_handler = HTTPCookieProcessor(cookie_obj)
# build_opener内部的实现就是urlopen
#  urlopen 只能进行简单的请求，不支持在线验证,cookie 代理IP等复杂操作
opener = build_opener(cookie_handler)
response = opener.open('http://www.neihanshequ.com')
print(response)
for cookie in cookie_obj:
    print('key:',cookie.name)
    print('value:',cookie)

