

import re
import random
from urllib.request import Request,urlopen,ProxyHandler,build_opener
base_url = 'https://www.qiushibaike.com/article/120699612/'
url_agen_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
 ]
headers = {
    'User-Agent':random.choice(url_agen_list)
}
# ip_list = [
#     '124.193.85.88:8080	',
#     '118.190.95.43:9001',
#     '121.42.167.160:3128',
#     '118.190.95.35:9001'
# ]
# proxies = {
#     'http:':random.choice(ip_list)
# }
def down_load_qibai_info():
    request = Request(base_url,headers=headers)
    # proxy_handler = ProxyHandler(proxies)
    # opener = build_opener(proxy_handler)
    # response = opener.open(request)
    response = urlopen(request)
    code = response.read().decode()
    pattern = re.compile(r'<div class="replay">.*?<a href="(.*?)".*?>',re.S)
    result = pattern.findall(code)
    print(result)
    for href in result:
        href = href.strip('\n')
        full_url = 'https://www.qiushibaike.com'+href
        print('评论人主页：',full_url)
down_load_qibai_info()








