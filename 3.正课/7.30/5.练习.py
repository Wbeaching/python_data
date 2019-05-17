import csv
rows = [['张三',14],['李四',25],['王五',35]]
with open ('test2.csv','w',newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in rows:
        writer.writerow(row)
with open('test2.csv','r') as read_file:
    reader = csv.reader(read_file)
    print(reader)
    print([row for row in reader])
# def write_data():
#     columns = int(input('请输入总列数'))
#     col_list = []
#     while True:
#         # for n in columns:
#         #     result = input('请输入第{}列数据'.format(n+1))
#         #     col_list.append(result)
#         col_list.append([input('请输入第{}列数据'.format(n+1))for n in range(columns)])
#         is_continue = input('是否继续？Y/N')
#         if is_continue !='Y':
#             break
#     print(col_list)
#     with open('test2.csv','w',newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         for row in col_list:
#              writer.writerow(row)
# write_data()
# data_dic = [{'name':'zhangsan','age':15},{'name':'lisi','age':30}]
# with open('dict.csv','w',newline='') as csv_file:
#     keys = []
#     for key in data_dic[0].keys():
#         print(key)
#         keys.append(key)
#     writer = csv.DictWriter(csv_file,fieldnames=keys)
#     writer.writeheader()
#     for dict in data_dic:
#         writer.writerow(dict)
# with open('dict.csv','r') as csv_file:
#     reader = csv.DictReader(csv_file)
#     print([row for row in reader])
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F')
driver.find_element_by_name('username').send_keys