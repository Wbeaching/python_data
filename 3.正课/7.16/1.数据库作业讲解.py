#
# 作业：在控制台输入信息，程序执行不同的命令：
# 控制台输入1：添加学生信息，学生所有信息需要通过控制台输入
# 控制台输入2：修改学生信息，需要在控制台指明哪一个学生的信息需要修改，
# 同时在控制台输入修改的内容
# 控制台输入3：删除学生的信息，需要在控制台指明那个学生的信息需要被删除
# 控制台输入4：查询所有学生的信息
# 控制台输入其他数字：推出查询系统
import  sqlite3
connect = sqlite3.connect('studentDB')
curosr = connect.cursor()
curosr.execute('create table if not exists student_info(name text ,age int ,phone int) ')
connect.commit()
# 关闭光标
curosr.close()
# 关闭数据库
connect.close()
def add_student_info_to_table():
    name = input('请输入学生姓名')
    age = int(input('请输入学生年龄'))
    phone = int(input('请输入学生联系方式'))
    # 重新连接到数据库
    connect = sqlite3.connect('studentDB')
    # 重新获取光标
    curosr = connect.cursor()
    curosr.execute('insert into student_info(name,age ,phone) VALUES ("{}","{}","{}")'.format(name,age,phone))
    connect.commit()
    curosr.close()
    connect.close()
    add_student_info_to_table()
def delete_student_info_table()    :
    name = input('请输入要删除的学生的名字')
    connect = sqlite3.connect('studentDB')
    curosr= connect.cursor()
    curosr.execute('delete from student_info VALUE name = "{}"'.format(name))
    connect.commit()
    curosr.close()
    connect.close()
    delete_student_info_table()
def update_student_info_to_table()    :
    select = input('请输入你想要的操作，0：全部修改，1：修改姓名')
    name = input('请输入你想更新的数据')
    new_name = input('请输入新的姓名')
    connect = sqlite3.connect('studentDB')
    curosr = connect.cursor()
    if select =='0':
        new_age = int(input('请输入新的年龄'))
        new_phone = int(input('请输入新的联系方式'))
        curosr.execute('update student_info set name="{}",age= "{}",phone="{}" VALUE name ="{}"'.format(new_name,new_age,new_phone,name))
    elif select =='1':
        curosr.execute('update student_info set name ="{}" VALUE NAME ="{}"'.format(new_name,name))
    else:
        print('命令无效')
        connect.commit()
        curosr.close()
        connect.close()
        update_student_info_to_table()
def get_all_info_table():
    connect = sqlite3.connect('studentDB')
    curosr = connect.cursor()
    curosr.execute('select*from student_info')
    connect.commit()
    print(curosr.fetchall())
    curosr.close()
    connect.close()
    get_all_info_table()
# 内存管理
# 内存的分区
# 堆
# 栈
# 常量区
# 全局区
# 方法区
# 代码里面的一切内容都放在内存中
# 对象用完以后要释放，否则会一直占用内存，造成系统/电脑性能下降
# 对象以什么样的准则进行释放内存？
# 管理内存的原则：
# 1.手动释放
# name = '小明'
# print(name)
# 2.自动释放
# java 垃圾自动回收机制
# def test ():
#     name = '小明'
# test()
# 3.引用计数
# python oc
print("""
学生信息管理系统
输入1：添加学生信息
输入2：修改学生信息
输入3：删除学生信息
输入4：查询所有学生信息
其他数字：退出查询系统
""")
while True:
    value = int(input('请输入你要执行的命令'))
    if value ==1:
        add_student_info_to_table()
    elif value ==2:
        update_student_info_to_table()
    elif value ==3:
        delete_student_info_table()
    elif value ==4:
        get_all_info_table()
    else:
        print('退出程序')
        break



