
# while 后面的判断条件
# 那么里面的代码块会一直执行

#while Ture
age = 1
while age <18:
    print('未成年{}'.format(age))
    age +=1

count = 0
while True:
    count+=1
    if count>=10000:
        #break打断
        #当循环里面执行了break
        #那么后面的循环都不执行
        break
    print(count)
    #break 跳出循环 循环外面的代码继续执行
    #continue 跳出这一次循环，剩下的循环继续执行
    #return 通常用在方法中 后面代码通通不执行
count = 0
while count<10:
    count+=1
    if count==4:
        print('count为{}'.format(count))
# return  不能在方法外面使用
# while True:
#     count +=1
#     if count == 20:
#         return
name = '小王'
age =16
# SyntaxError: invalid syntax
#字符串错误，+后面必须跟字符串
#解决办法：使用+必须使用字符串，或者将数字转化成字符串
print('我的名字是'+name +',我的年龄是'+age)
for index in range(10):
    if name =='小王':
        print('hello')
    else:
        print('nothing')
# for 后面循环的范围/次数，注重自己来循环的次数
# while 后面写判断的条件，主要是条件的真假




























