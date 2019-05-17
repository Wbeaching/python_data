                                                                                                                                                                                                                               # 总结：xpath和bs4和正则的区别
# 总结：数据方式的区别
# 举例说明
from urllib.request import urlretrieve
import os,shutil
import requests
from lxml import etree
if os.path.exists('images'):
    shutil.rmtree('images')
os.mkdir('images')
os.chdir('images')
currnt_page = 1
def get_image_with_code(url):
    global currnt_page
    response = requests.get(url).text
    # print(response)
    code = etree.HTML(response)
    img_list = code.xpath('//div[@class="il_img"]/a/img')
    print('正在下载第{}页'.format(currnt_page))
    # 创建对应页面的文件夹
    os.mkdir('Page{}'.format(currnt_page))
    os.chdir('Page{}'.format(currnt_page))
    for img in img_list:
        # img_src = img.get('src')
        img_src = img.xpath('@src')[0]
        img_alt = img.xpath('@alt')[0]
        urlretrieve(img_src,img_alt+'.jpg')
    currnt_page += 1
    os.chdir(os.path.pardir)
    # 如果还有下一页则返回
    # 如果没有下一页则返回一个空[]
    next_page_url = code.xpath('//a[@class="page-next"]')
    # print(next_page_url)
    if len(next_page_url) == 0:
        print('已经最后一页')
        return
    href = next_page_url[0].get('href')
    print(href)
    full_ur = 'http://www.ivsky.com'+href
    get_image_with_code(full_ur)
get_image_with_code('http://www.ivsky.com/tupian/meishishijie/')
# 爬虫流程：
# 1.拼接url
# 2.获取User-Agent，设置代理ip
# 3.请求url，urlopen，requests
# 4.获取响应 (response,response.read() response.content  response.text)\
# 5.获取源码中指定数据(re  ,xpath  ,bs4)
# 6.美化数据  正则  strip
# 7.保存  （文件读写  ，sqlit3  ，lxml）