
# object 任何一个对象都直接或间接继承自object
# java
# oc
# 从功能上定义：类是属性和方法的集合
class Hero(object):
    blood = 700
    attact = 67
    level = 1
    def skill(self):
      print('致盲射击')
timo = Hero()
timo.skill()
print(Hero.blood)
print(Hero.blood)
class People(object):
    # init 初始化
    # 当对象创建的时候，属性的默认值
    # 魔术方法
    count= 0
    def __init__(self,name ,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        # 对象方法
    def sleep(self):
        print('{}一天要睡十七八个小时'.format(self.name))
    def work(self):
        print('工作时间段，不开心')
    def fond(self):
        print('人生苦短，及时行乐')
# 对象创建的时候，会自动调用init 方法
# 如果init 方法需要参数的话
# 那么对象创建的时候也要参数
ZhangSan = People('张三','男',17)
ZhangSan.sleep()
Lisi = People('李四','女',21)
Lisi.sleep()
print(People.count)
# 类属性可以通过对象来调用
print(Lisi.count)
People.work(ZhangSan)
# work方法是People里面的对象方法 self 指的是People的对象
# 所以在调用方法的时候，需要传入一个People对象
class Person(object):
    # 如果在初始化的时候 设置了默认值
    # 那么在创建的对象的时候 可以不必设置参数
    def __init__(self,name = '',age ='',sex ='',fond = ''):
        self.name = name
        # 属性前面添加下划线，这种方式叫私有属性
        # 不想叫别人访问
        # 这种属性不是绝对访问不了
        # 可以通过属性前面添加下划线方式访问
        self._age = age
        self._sex = sex
        # 属性如果是双下划綫，想要调用属性
        # 需要通过p1__Person__fond这种方式调用
        self.__fond = fond

    # property属性
    # attribute属性
    # argument参数
    # 声明get set方法的标记

    @property
    def fond(self):
        print('get方法被调用')
        return self.__fond
    @fond.setter
    def fond(self, fond):
        print('set方法被调用了')
        self.__fond = fond
            # get方法
p1 = Person('张三丰',149,'男','练剑')
print(p1.name)
print(p1._age)
print(p1._sex)
print(p1._Person__fond)
print(p1.fond)

