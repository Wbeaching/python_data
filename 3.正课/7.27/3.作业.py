
# 总结：xpath bs4 和正则的区别
# 总结：请求方式的区别
# 举例说明
from urllib.request import Request,urlopen,urlretrieve
from lxml import etree
import requests
from bs4 import BeautifulSoup
import re,os,shutil
if os.path.exists('tupian'):
    shutil.rmtree('tupian')
os.mkdir('tupian')
os.chdir('tupian')
current_page = 1
url = 'https://www.meishij.net/chufang/diy/?&page=1'
headers =  {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
response = requests.get(url,headers =headers).content
# print(response)
code = etree.HTML(response)
image_list =code.xpath('//div[@class="listtyle1"]/a')
# print(image_list)
os.mkdir('Page{}'.format(current_page))
os.chdir('Page{}'.format(current_page))
for image in image_list:
    image_alt = image.xpath('img/@alt')[0]+'.jpg'
    image_src = image.xpath('img/@src')[0]
    name = image.xpath('div/div/div/span/text()')[0].split(' ')[3]+'人气'
    print('菜名:{}({})\n{}'.format(image_alt,name,image_src))
    # urlretrieve(image_src,image_alt,name)
# os.chdir(os.path.pardir)
#
#


# soup = BeautifulSoup(response,'lxml')
# new_list = soup.select('div.listtyle1 a img')
# name = soup.div.a.img.string
# print(name)
# print(new_list)
# for image in new_list:
#     image_alt = image.get('alt')
#     image_src = image.get('src')
    # name = image.se
    # print(image_alt)
    # print(image_src)

# request = Request(url,headers=headers)
# response = urlopen(request)
# code = response.decode()
# patternn = re.compile('<div class="listtyle1".*?>.*?<a.*?>.*?<img.*?alt="(.*?)".*?src="(.*?)".*?>.*?<div class="c1".*?>.*?<span>.*?评论.*?(.*?)</span>',re.S)
# result = patternn.findall(code)
# print(result)
# for image in result:
#     image_alt = image[0]
#     image_src = image[1]
#     image_name = image[2]
#     print('{}{}\n{}'.format(image_alt,image_name,image_src))

