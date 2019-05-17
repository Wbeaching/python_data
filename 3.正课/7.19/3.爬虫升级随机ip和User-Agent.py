
import random
from urllib.request import Request,urlopen,ProxyHandler,build_opener
url_agent_list=[
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36',
]
headers = {
'User-Agent':random .choice(url_agent_list)
}
ip_list = [
    '101.236.23.202:8866',
    '61.135.217.7:80',
    '111.155.116.234:8123',
    '122.114.31.177:808'
]
proxies = {
    'http:':random.choice(ip_list)
}
# 设置爬虫目标
request =Request('http://www.baidu.com',headers = headers)
# 创建IP代理对象
proxy_handler = ProxyHandler(proxies)
# urlopen 不支持http高级函数，cook,验证,代理等内容
opener = build_opener(proxy_handler)
response  = opener.open(request)
print(response.read().decode())