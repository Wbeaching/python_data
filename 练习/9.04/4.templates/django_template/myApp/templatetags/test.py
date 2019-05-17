from django.template import Library
# 注册当前的数据 注册完以后必须重新 否则程序可能会崩溃
register = Library()
@register.filter
def add(value):
    pass