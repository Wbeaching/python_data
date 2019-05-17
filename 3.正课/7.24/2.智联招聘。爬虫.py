from urllib.request import Request,urlopen
from urllib.parse import quote
import re
# 处理Excele文件必须的模块
import xlwt
import string
# 目的：1.爬取数据 2.存储到excel
class ZLZP(object):
    def __init__(self,citylist=[],workname=''):
        self.citylist = citylist
        self.workname = workname
        self.base_name = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
        self.citystring = ''
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }
        self.total_page = 1
        self.currentIndex =1
        for cityName in self.citylist:
            if cityName == self.citylist[:-1]:
                self.citystring += quote(cityName)
            else:
                self.citystring += quote(cityName)
                self.citystring+='%2B'

    def start_spider(self):
        # 第一次调用该方法 传值1
        code=self.get_code_with_url(1)
        self.get_total_page(code)
        # self.open_excel_file()
        # print(code)
        sheet ,workBook = self.open_excel_file()
        # 获取每一页数据
        record_row =1
        for index in range(1, self.total_page + 1):
            code = self.get_code_with_url(index)
            if code == None:
                continue
            result_list = self.get_all_data(code)
            # 获取具体的每一条数据
            for job ,company ,salary,location in result_list:
                sheet.write(record_row,0,job)
                sheet.write(record_row,1,company)
                sheet.write(record_row,2,salary)
                sheet.write(record_row,3,location)
                record_row+=1
        workBook.save('python职位表.xls')
    def get_all_data(self,code):
        pattern = re.compile(r'<table.*?class="newlist".*?>.*?<td class="zwmc".*?>.*?<a.*?>(.*?)</a>.*?<td class="gsmc">.*?<a.*?>(.*?)</a>.*?<td class="zwyx">(.*?)</td>.*?<td class="gzdd">(.*?)</td>',re.S)
        result = pattern.findall(code)
        print(result)
        list = []
        for value in result:
            jobName = value[0]
            companyName = value[1]
            salary = value[2]
            location = value[3]
            pattern = re.compile(r'<.*?>',re.S)
            jobName = re.sub(pattern,'',jobName)
            companyName = re.sub(pattern,'',companyName)
            list.append([jobName,companyName,salary,location])
        return list


    def open_excel_file(self):
        # 创建工作表对象，并设置编码方式为utf-8
        workBook = xlwt.Workbook(encoding='utf-8')
        sheet = workBook.add_sheet('python职位表')
        # 值1：行  索引0开始
        # 值2：列  索引从0开始
        # 值3：标题
        sheet.write(0,  0 , '职位名称')
        sheet.write(0 , 1, '公司名称')
        sheet.write(0 , 2, '薪资水平')
        sheet.write(0 , 3 ,'工作地点')
        return sheet,workBook
    def get_total_page(self,code):
        # pattern = re.compile(r'<table class="newlist".*?>.*?<td class="zwmc".*?>.*?<a.*?>(.*?)</a>',re.S)
        pattern = re.compile(r'<span class="search_yx_tj">.*?<em>(.*?)</em>',re.S)
        result = pattern.findall(code)
        # print(len(result))
        print(result)
        number = int(result[0])

        # number =len(result)
        if number % 60==0:
            self.total_page =number//60
        else:
            self.total_page = number//60+1
        print(self.total_page)
    def get_code_with_url(self,pageIndex):
        full_url= self.base_name+'jl='+self.citystring+'&kw='+self.workname+'&p='+str(pageIndex)
        print(full_url)
        request = Request(full_url,headers=self.headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('请求失败',e)
        else:
            return code
citys = []
while True:
    city = input('请输入你去的城市')
    if city =='E':
        break
    citys.append(city)
job = input('请输入你喜欢的工作')
zp = ZLZP(citys,job)
zp.start_spider()