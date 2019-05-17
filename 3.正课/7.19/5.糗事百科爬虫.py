
import re
import random
from urllib.request import Request,urlopen,ProxyHandler,build_opener
base_url = 'https://www.qiushibaike.com/hot/page/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
ip_list = [
    '124.193.85.88:8080	',
    '118.190.95.43:9001',
    '121.42.167.160:3128',
    '118.190.95.35:9001'
]
proxies = {
    'http:':random.choice(ip_list)
}
def down_load_qiubai_info(page):
    full_url = base_url+str(page)+'/'
    request = Request(full_url,headers =headers)
    response = urlopen(request)
    # 获取对应网页的内容
    code = response.read().decode()
    # 正则匹配的内容 从指定的开始的位置 到全部结束的位置
    # 所以只需要指定开始的位置，不需要指定结束的位置
    #
    # 如果我们想要正则获取某一堆标签里面的内容的时候
    # 南无要将这一对标签写完整 而且在想要获取的内容
    # 上添加（）列入：<h2>(.*?)</h2>
    # print(code)
    # pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?Icon">(.*?)</div>',re.S)
    # result = pattern.findall(code)
    # # print(result)
    # for name,age in result:
    #     name = name.strip('\n')
    #     age = age.strip('\n')
    #     print('作者是:',name)
    #     print('年龄是:',age)
    pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?Icon">(.*?)</div>'
                         r'.*?<a href="(.*?)".*?>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats">.*?'
                         r'<i class="number">(.*?)</i>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S)
    result = pattern.findall(code)
    for name,age ,href,content,number,comment in result:
        name = name.strip('\n')
        age = age.strip('\n')
        content = content.strip('\n')
        number = number.strip('\n')
        print('作者是：',name)
        print('年龄是：',age )
        print('详情是：',href)
        print('内容是：',content)
        print('人数是：',number)
        print('评论数：',comment)
        if int(comment) !=0:
            get_all_comment_with(href)
        else:
            print('该内容暂无评论')
def get_all_comment_with(url):
    detail_url = 'http://www.qiushibaike.com'+url
    print(detail_url)
    request = Request(detail_url,headers =headers)
    proxy_handler = ProxyHandler(proxies)
    opener = build_opener(proxy_handler)
    response = opener.open(request)
    # response = urlopen(request)
    code = response.read().decode()
    # print(code)
    pattern = re.compile(r'<a.*?class="userlogin".*?title="(.*?)">.*?<span class="body">(.*?)</span>',re.S)
    result = pattern.findall(code)
    print(result)
down_load_qiubai_info(1)


 