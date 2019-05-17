import time
# time.struct_time结构体
time1 = time.localtime()
print(time1)
# 1970年到现在的秒数
time2 = time.time()
print(time2)
# 从1970年开始往后指定的秒数
time3 = time.localtime(1531247000)
print(time3)
result = time.strftime('%y %m %d %H %M %S',time.localtime())
print(result)

# 线程休眠
# 爬虫：获取对方数据太快，有可能被认为爬虫程序，
#    所以在爬虫时有时候需要减缓速度
# 线程：A代码块的执行受B代码的影响，必须确保B代码先执行并返回数据，
# 这时候可以让A先休眠一段时间（注意：休眠不是必须的，也不是最好的）
# 定时任务：需要代码到指定时间，是去执行某个任务，
# 当时间还未到达，可以让时间先休眠
# time.sleep(3)
# print('今天是周三，一星期马上过去一半了')
import datetime
# data 数据
# date 日期
date1 = datetime.datetime.now()
print(date1)
date2 = date1.strftime('%y %m %d %H:%M:%S')
print(date2)
date2 = date1.strftime('%y year %m month %d day %H hour %M minute %S second')
print(date2)
# UnicodeEncodeError: 'locale' codec can't encode character '
# \u5e74' in position 2: Illegal byte sequence
# 编码错误：本地文件不能对指定位置的字符进行编码
date2 = date1.strftime('%yyear %mmonth %dday ')
print(date2)
date2 = date2.replace('year','年').replace('month','月').replace('day','日')
print(date2)
# 怎么获取今天往后推的时间
# 可以用来计算过期时间
# timedelta 推迟
date4 = datetime.timedelta(days=1,hours=12)
date5 = datetime.datetime.now()+date4
print(date5)
date6 = datetime.datetime.now()
date7 = date6.date()
print(date7)
print(date7.year,date7.month,date7.day)
date8 = date6.time()
print(date8)
# stamp 时间戳
# timestamp 时间戳，时间线
date9 = datetime.datetime.now()
print(date9.timestamp())
