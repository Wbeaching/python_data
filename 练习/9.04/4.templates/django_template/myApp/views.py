from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
class People(object):
    def __init__(self ,name ,age):
        self.name = name
        self.age = age
def index(request):
    p = People('小明',9)
    newTime = datetime.datetime.now()
    content = {
        'name':'张三',
        'font_list':['吃饭','睡觉','玩手机','看视频','扯淡'],
        'friend' : p ,
        'today':newTime ,
        'girl_friend':{
            'name':'小美',
            'height':160,
            'hasKuang':True
        }
    }
    # return HttpResponse('asdasdasdasdsad')
    return render(request,'add.html',content)
