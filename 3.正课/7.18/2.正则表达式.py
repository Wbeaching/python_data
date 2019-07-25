
import re
# 正则表达式
# 正则表达式可以表达判断目标字符串是否符合特定
# 的要求，比如判断是否是手机号，身份证号，邮箱号

"""
digit  数字
\d：表示任意的一位数字
\d\d:表示两位数字
world   字母
\w:表示任意的字母和数字
space 表示空格
\s:表示空格
. :表示任意的内容1,23,4,as,df,fg
a. :在a后面匹配任意的内容  ab  al  a2  ac ad
*: 表示内容出现0次到多次
a.*:a  al  ab  aaaa  alllll  abbbbb
+:表示内容出现一次到多次
a.+:  aa  ab  al  ac   ad
？:表示内容出现0次到1次
a.?: a   al  a9
^  :表示以。。。。开头
$ :表示以。。。。结尾
{n} :表示内容重复n次
\d\d\d
\{3}
{n,m} :标志最少重复n次 ，最多重复m次
\d{3,5}
{n,} :表示最少重复n次
{,m} :表示做多重复m次
"""
# pattern 模式
# compie 编译
# 后面写正则表达式的内容
# （）代表从目标字符串当中获取的子串
#   每一个（）就是一个group组
pattern = re.compile('(\d+)(\w+)')
content = '123helloworld'
# match 匹配
result = re.match(pattern,content)
if result:
    # 返回的是一个匹配的对象
    print(result)
    print('------------------------')
    # 返回的符合要求的全部内容
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))
else:
    print('不符合')

pattern = re.compile('my')
result = re.match(pattern,'myself')
print(result.group(0))
# match匹配的是内容开始部分
# 作用等于 startwith
result = re.match(pattern,'love  myself')
print(result)
print('--------------')
pattern = re.compile('lalala')
result = re.match(pattern,'lalalaha')
print(result)
pattern= re.compile('my')
result = pattern.match('myself')
print(result.group(0))
# 贪婪模式与非贪婪模式
# 正则表达式默认为贪婪模式，尽量找到所有的
# 符合要求的内容
# .* :称为贪婪模式
print('------------------------------------------------')
content = 'aabababab11b222'
pattern = re.compile('(a.*b)')
result = pattern.match(content)
print(result)
# .*? :称为非贪婪模式
# 任意字符出现0次或多次直到遇见第一个b  结束
pattern = re.compile('(a.*?b)')
result = pattern.match(content)
print(result)
# 匹配任意字符开头
# 后面找到一个以b开始以b结尾的内容
pattern = re.compile('.*?(b.*?b).*?')
result = pattern.match(content)
print('**********')
print(result.group(0))
print('************')
# * + 同为贪婪模式
# * 至少0次，至多无限次
# + 至少1次 ，至多无限次
pattern = re.compile('(a.+b)')
result = pattern.match(content)
print(result)
print('---------------------------')
print('hello \n world')
# raw string 会将字符串里面的转义字符输出出来
print(r'hello \n world')
title = '123hello world'
# pattern = re.compile(r'\d\d\d')
pattern = re.compile(r'\d{3}')
result = pattern.match(title)
print(result.group(0))
# 匹配全国固话 0371-66666666
pattern = re.compile(r'(\d{4})-(\d{8})')
result = pattern.match('0371-68686888')
print(result.group(0))
print('**********')
print(result.group(1))
print(result.group(2))
# |或者 设置用于不同情况的正则
pattern = re.compile('((haha|heihei)balabala)')
result = pattern.match('heiheibalabala')
print(result)
# search 找到字符串当中第一个负责正则的内容
# 注意：只找到第一个
pattern = re.compile(r'http')
result = pattern.search('www.jd.com,http://www.taobao.com')
print(result)
print('1111111111111111111111111111111111111111')
pattern = re.compile(r'you')
result = pattern.search('I love you ,I miss you , I hate you')
print(result.group(0))
pattern = re.compile(r'I')
result = pattern.search('love you I')
print(result)
# findall 找到所有符合的内容
content = '12345,上山打老虎，老虎没打着，打只小松鼠，55555'
pattern = re.compile(r'\d{5}')
result = pattern.findall(content)
print(result)
print('22222222222222')
# sub :替换子串（字符串的一部分）
# \s :匹配空白的内容
content = '杨过对战金轮法王，郭靖观战'
pattern = re.compile(r'杨\s*过')
result = pattern.sub('吕布',content)
print(result)
print('8888888888888888888')
pattern = re.compile(r'金轮法王')
result = pattern.sub('服部半藏',result)
print(result)
print('999999999999999999999')
key_word= [
    (r'杨\s*过','吕布'),
    (r'金轮法王','服部半藏'),
    (r'郭靖','东方不败')
]
for pattern,replace in key_word:
    pattern = re.compile(pattern)
    content = pattern.sub(replace,content)
    print(content)
# 匹配手机号
pattern = re.compile(r'^((13[0-9])|(14[6,7])|(15[0-3,5-9])|(18[0|5-9]))\d{8}$')
result = pattern.match('14730314989')
print(result.group(0))
