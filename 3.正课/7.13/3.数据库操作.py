

# 内存：变量 str list dict tuple 文件
# 常见存储数据的三种方式
# 1.内存存储：变量  有点 ：读写速度快 缺点：程序关闭 ，内存释放
# 2.文件存储：文件读写操作  有点： 数据永久  缺点：读写操作麻烦
# 数据库即为数据存储库
# 3.数据库存储  有点：数据永久 缺点：难度大
#  数据库按性质划分
# 1.关系型数据库：数据库与数据之间有着紧密米练习
#  有点：可以进行多表查询  缺点： 删除数据维护麻烦 牵一发动全身
# 2.费关系型数据库：数据与数据之间没有联系
# 有点：对数据进行增删维护简单  缺点：数据值减少了耦合性
# 一人吃饱，全家不饿  mongDB  redis
#
# 数据库按使用规模划分可以划分为四个等级
# 1.大型数据库 一般用于大型商业公司 例如淘宝，京东 代表：oracl
# 中型数据库 使用非常广泛的数据库  代表 SQLServer
# 3.小型数据库 一般用于晓得产品公司或者公司内部数据库 代表 sq
# 4.微型数据库
#
#
#
import  sqlite3
# 创建一个数据库
con = sqlite3.connect('myDB')
# 创建一个数据库光标
# 使用光标对数据表进行增删改查等操作

cursor = con.cursor()
# 使用光标执行命令：创建一张表 如果不存在的话
cursor.execute('CREATE TABLE IF NOT EXISTS myTable (name text ,age int) ')
con.commit()
# insert into  插入数据到指定表中
cursor.execute('INSERT INTO  myTable(name,age) VALUES ("luxun",17)')
con.commit()













