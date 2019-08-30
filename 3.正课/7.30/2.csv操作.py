

# comma  sepreated value 逗号分隔值
# [1,2,3]{'name':'张三','age':'14'}
import csv
rows = [['张三',14],['李四',24],['王五',34]]
# csv在写入的时候，默认每次写入会空一行作为分割
# 使用newline =''可以将空行去掉
with open ('test1.csv','w',newline = '') as csv_file:
    writer = csv.writer(csv_file)
    for row in rows:
        # writerow 写入一行
        writer.writerow(row)

with open('test1.csv','r') as read_file:
    # 获取一个csv对象进行内容读取
    reader = csv.reader(read_file)
    print(reader)
    print([row for row in reader])

def write_data():
    columns= int(input('请输入总列数'))
    col_list = []
    # for index in range(columns):
    while True:
        # for n in columns:
        #     result= input('请输入第n列数据'.format(n+1))
        #     col_list.append(result)
        col_list.append([input('请输入第{}列数据'.format(n+1))for n in range(columns)])
        is_continue = input('是否继续？Y/N')
        if is_continue !='Y':
            break
            # continue 跳出本次循环，下次循环继续执行
            # return  结束循环和方法 return后面的代码统统不执行
    print(col_list)
    with open ('test2.csv','w')as csv_file:
        writer = csv.writer(csv_file)
        for row in col_list:
            writer.writerow(row)
write_data()

data_dic = [{'name':'zhangsan','age':'15'},{'name':'lisi','age':'25'}]
with open('dict.csv','w',newline='') as csv_file:
    keys = []
    for key in data_dic[0].keys():
        print(key)
        keys.append(key)
     # 写入一个字典到csv中 （excel）fieldnames 设置文本标题
    writer = csv.DictWriter(csv_file,fieldnames=keys)
    # 开始写入标题
    writer.writeheader()
    for dict in data_dic:
        writer.writerow(dict)

with open('dict.csv','r') as csv_file:
    reader = csv.DictReader(csv_file)
    print([row for row in reader])

