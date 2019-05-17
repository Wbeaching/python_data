

# requests是对urllib3的封装
import requests
url = 'http://www.baidu.com'
# get 和 post请求
reponse = requests.get(url)
print(reponse)
# 获取网页文本内容
print(reponse.text)
# reason 原因
# 请求状态的说明
print(reponse.reason)
# links 跳转的地址
print(reponse.links)
# 之前的请求历史
print(reponse.history)
# 获取网页的编码格式
print(reponse.apparent_encoding)
# 设置响应的编码格式为网页的编码格式
reponse.encoding = reponse.apparent_encoding
# 获取网页得内容（buytes形式的)
print(reponse.content)
# 获取网页cookie
print(reponse.cookies)
# 获取响应头信息
print(reponse.headers)
# 获取请求网址
print(reponse.request.url)