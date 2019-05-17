import requests
import json
from prettyprinter import pprint
class Weather(object):
    def __init__(self):
        self.location_url = 'http://api.map.baidu.com/location/ip?&ak=KQvhEkxc6mFCAYHTblC3NGVmxzxIWk0E&coor=bd09ll'
        self.weather_url = 'http://api.map.baidu.com/telematics/v3/weather?output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?&location='
    def start_spider(self):

        cityName =self.get_location()
        self.get_weather_info(cityName)
        while True:
            cityName = input('请输入城市的名字')
            if cityName == 'E':
                return
            self.get_weather_info(cityName)
    def get_location(self):
        response = requests.get(self.location_url)
        # print(respose)
        # print(respose.content)
        result_dic = json.loads(response.content)
        # pprint(result_dic)
        city = result_dic['content']['address_detail']['city']
        return city
    def get_weather_info(self,cityName):
        url = self.weather_url+cityName
        response = requests.get(url)
        weather_dic = json.loads(response.content)
        # pprint(weather_dic)
        for dayDic in weather_dic['results'][0]['weather_data']:
            print('{}'.format(dayDic['date']))
            print('温度{}'.format(dayDic['temperature']))
w= Weather()
w.start_spider()