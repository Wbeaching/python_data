# 作业：奇书网 ，玄幻奇幻类小说
# 将小说名，点击次数，文件大小，书籍类型。更新日期，连载状态。书籍作者，小说简介，下载地址存储到excel里面
from lxml import etree
import requests,xlwt
class QSWSpider(object):

    def __init__(self):
        self.base_url = 'https://www.qisuu.la/'
        self.headers = {
            'User-Aget':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
        self.current_page = 1

    def start_spider(self):
        first_page = 'soft/sort01/index_1.html'
        self.get_page_code_with_url(first_page)

    def get_page_code_with_url(self,url):
        url = self.base_url+url
        # print(url)
        response = requests.get(url,headers = self.headers).content
        code = etree.HTML(response)
        # print(code)
        self.get_info_with_url(code)

    def get_info_with_url(self,code):
        name_list = code.xpath('//div[@class="listBox"]/ul/li/a')
        for name in name_list:
            # print(name)
            name_href = name.xpath('@href')
            content = name_href[0]
            # print(content)
            self.get_code_with_url(content)

    def get_code_with_url(self,content):
        full_url = self.base_url+content
        # print(full_url)
        response = requests.get(full_url,headers = self.headers).content
        code = etree.HTML(response)
        # print(code)
        self.get_info_with_code(code)

    def get_info_with_code(self,code):
        image_list = code.xpath('//div[@class="detail_right"]/h1')
        # print(image_list)
        for image in image_list:
            name = image.xpath('//h1/text()')[0]
            # print(name)
            list=image.xpath('//li[@class="small"]/text()')[:-1]
            # print(list)
            dianji = list[0]
            daxiao = list[1]
            leixing = list[2]
            gengxin = list[3]
            lianzai = list[4]
            zuozhe = list[5]
            # print(dianji)
            # print(daxiao)
            # print(leixing)
            # print(gengxin)
            # print(lianzai)
            # print(zuozhe)
        jieshao_list = code.xpath('//div[@class="showInfo"]/p/text()')[0].strip('\n').replace('u3000','').replace(' ','')
        # print(jieshao_list)
        xiazai_list = code.xpath('//div[@class="showDown"]/ul/li')
        for xiazai in xiazai_list:
            zaixian = xiazai.xpath('//li/div[@class="tabBox"]/text()')
            txt = xiazai.xpath('//li[@style="height: 20px;"]/b/text()')
            # print(zaixian)
            # print(txt)
        self.current_page+=1
        self.get_next_page(code)

    def get_next_page(self,code):
        next_page = code.xpath('//div[@class="tspage"]/a/@href')
        print(next_page)
        # if len(next_page) == 0:
        #     print('已经是最后一页')
        #     return
        # self.get_page_code_with_url(next_page)

qishu = QSWSpider()
qishu.start_spider()

