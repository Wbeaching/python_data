




# 声明方法1：
# 创建一个txt文件，里面存放1000条数据，每条数据长度为10 包含的小写字母和数字
# 声明方法2：
# 读取txt文件里面的所有数据，如果该条数据只有数字，那么创建一个txt文件，保存起来
# 声明方法3：
# 读取txt文件里面的所有数据，如果该条数据只有字母，那么创建一个txt文件，保存起来
# 声明方法4：
# 读取txt文件里面的所有数据，如果该条数据包含数字和字母，那么创建一个txt文件，保存起来\
import random
str = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
def AllChar():
    with open('data.txt','w',encoding='utf-8') as f:
        for x in range(1000):
            content = ''
            for y in range(10):
                char_str = random.choice(str)
                content += char_str
        f.write(content+'\n')
    f.close()
def readAllChar():
    list = []
    with open('data.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            line = line[0:10]
            list.append(line)
    f.close()
    return list
readAllChar()
def getchar():
    list = readAllChar()
    with open('data3.txt','w') as f:
        for value in list:
            count = 0
            for char in value:
                if (ord(char)>=65 and ord(char)<=90 or ord(char)>=97 and ord(char)<=122):
                    count += 1
                    print(count)
            if count ==10:
                f.write(value+'\n')
getchar()
def getchar():
    list = readAllChar()
    with open('data2.txt','w') as f:
        for value in list:
            if value.isalpha():
                f.write
    f.close()
getchar()
def getchar():
    list = readAllChar()
    with open('data3.txt','w') as f:
        for value in list:
            count = 0
            for char in value:
                if (ord(char)>=65 and ord(char)<=90 or ord(char)>=97 and ord(char)<=122):
                    count += 1
                    print(count)
            if count ==10:
                f.write(value+'\n')
getchar()
def getchar():
    list = readAllChar()
    with open('data4.txt','w') as f:
        for value in list:
            isallchar = True
            for char in value:
                if char.isdigit():
                    isallchar =False
                    break
            if isallchar == True:
               f.write(value+'\n')
    f.close
getchar()
def getnumwithchar():
    list = readAllChar()
    with open('data5.txt','w') as f:
        for value in list:
            if not value.isalpha() and  not value.isdigit():
                f.write(value+'\n')
    f.close()
getnumwithchar()















