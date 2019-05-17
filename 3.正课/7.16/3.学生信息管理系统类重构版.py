
import sqlite3
class student(object):
    def __init__(self,name ='',age ='',tel = ''):
        self.name = name
        self.age = age
        self.tel = tel
    def say(self):
        print('我说：我的名字是'+self.name)
    def work(self):
        print(self.name +'是游戏主播')
class DBAction(object):
    def __init__(self,dbname ='',tablename =''):
        self.dbname = dbname
        self.tablename = tablename
        self.connect = None
        self.curosr = None
    def createDBAndTable(self):
        self.connect =sqlite3.connect('{}'.format(self.dbname))
        self.curosr = self.connect.cursor()
        self.curosr.execute('create table if not exists"{}" (name text,age text,tel text)'.format(self.tablename))
    def commitAndClose(self):
        self.connect.commit()
        self.curosr.close()
        self.connect.close()
    def openDB(self):
        self.connect = sqlite3.connect('{}'.format(self.dbname))
        self.curosr = self.connect.cursor()
    # def makeFriendWithBody(self,other):
    #         pass
    # def work(self,info):
    def addNewStudentToTable(self,student):
        # print('上班打卡')
        self.openDB()
        # print('我今天的工作是{}'.format(info))
        self.curosr.execute('insert into "{}" (name ,age ,tel) VALUES ("{}","{}","{}")'.format(self.tablename,student.name ,student.age,student.tel))
        # print('下班打卡')
        self.commitAndClose()
    def deleteStudentToTable(self,student):
        self.openDB()
        self.curosr.execute('delete from "{}" WHERE  name = "{}"'.format(self.tablename,student.name))
        self.commitAndClose()
myDB = DBAction('BDAction','tableAction')
myDB.createDBAndTable()
while True:
    value = input("""
     请输入操作：
     1.增加学生信息
     2.删除学生信息
     3.修改学生信息
     4.查看学生信息
   """ )
    value = int(value)
    if value==1:
        name = input('请输入姓名')
        age = input('请输入年龄')
        tel = input('请输入联系方式')
        student = student(name ,age ,tel)
        # s.work
        myDB.addNewStudentToTable(student)
    if value ==2:
        name = input('请输入要删除的学生信息')
        myDB.deleteStudentToTable(student)