
import shutil,os,re
from bs4 import BeautifulSoup


from urllib.request import Request,urlopen,urlretrieve
class Image_downLoad(object):
    def __init__(self):
        self.base_url = 'https://www.douyu.com/directory'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    def start_spider(self):
        code = self.get_code_with_url()
        self.get_info_with_code(code)
    def get_code_with_url(self):
        full_url = self.base_url
        request= Request(full_url,headers=self.headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('请求失败',e)
        else:
            # print(code)
            return code
    def get_info_with_code(self,code):
        pattern = re.compile(r'<a target="_blank".*?>.*?<p class=".*?">(.*?)</p>.*?<li class="unit".*?>.*?<img.*?data-original="(.*?)".*?>.*?</img>',re.S)
        result = pattern.findall(code)
        # print(result)
        for key in result:
            image_name = key[0]
            image = key[1]
            print(image_name,image)
        # soup = BeautifulSoup(code,'lxml')
        # image_list = soup.select('li.unit a img')
        # # print(image_list)
        # for image in image_list:
        #     image_data = image.get('data-original')
        #     print(image_data)
        # print(name+image_data)
DouYu = Image_downLoad()
DouYu.start_spider()


