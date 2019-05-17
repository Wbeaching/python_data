from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # 注意 url和path的区别
    # http://localhost:8000/index/justtest/?id=100&name=lisi
    url('justtest/',views.justTest) ,
    # http://localhost:8000/index/second/100/test
    url(r'second/(\d+)/(\w+)',views.second) ,
    # path(r'second/<mid>/<name>',views.second) ,

    # http://localhost:8000/index/third/10/11/wangwu
    url(r'third/(?P<a>\d+)/(?P<b>\d+)/(?P<name>\w+)',views
        .third)
]
# def test(a=0 , b=0 ,c=0):
#     pass
# test(b=10,a=1)