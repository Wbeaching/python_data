





# 从能上定义：类是属性和方法的集合
class Hero(object):
    # 属性 成为类属性
    a,b = 100,200
    blood = 700
    attact = 67
    level = 1
    def skill(self):
        print('致盲射击')
time = Hero()
time.skill()
print(time.blood)
print(Hero.blood)
class People(object):
    count = 0
    def __init__(self,name ,sex, age ):
        self.name = name
        self.sex = sex
        self.age = age
    def sleep(self):
        print('{}一天要睡十七八个小时'.format(self.name ))
    def work(self):
        print('工作时间短，不开心')
    def fond(self):
        print('人生苦短，及时行乐')
P=People('张三','男',18)
P.sleep()
# 类属性可以通过对象来调用
print(P.count)
# 对象属性只能通过对象来调用，不能通过类名+属性来调用
# print(People.name)
P.work()
# 类在调用方法的时候 后面要跟一个类的对象
People.work(P)
class Person(object):
    def __init__(self,name ='',age = '',sex = '',fond = ''):
        self.name = name
        # 前面添加下划线的叫做私有属性
        # 可以再属性前添加下划线的方式来调用
        self._age = age
        self._sex = sex
        self.__fond = fond
    @property
    def fond(self):
        print('get方法被调用了')
        return self.__fond
    @fond.setter
    def fond(self,fond):
        print('set方法被调用了')
        self.__fond = fond
p1 = Person('张三丰',149,'男','练剑')
print(p1.name)
print(p1._age)
print(p1._Person__fond)
print(p1.fond)
p1.fond = '练拳'
p1.name
p1.name = '123'
# object 祖类或者父类
# 子类能够继承父类的属性和方法
class People(object):
    def __init__(self,name = '',sex = '',age = ''):
        self.name = name
        self.age = age
        self.sex = sex
    def eat(self):
        print('活着的目的是为了吃')

class Man(People):
    def __init__(self,name ='',sex = '',age = '',huzi =''):
        self.huzi = huzi
        # 继承父类的属性
        super(Man,self).__init__(name ,sex ,age)
    def eat(self):
        super(Man,self).eat()
        print('我张三丰饿死也不吃你们一口饭')
    def makeFriendWithOtherPeople(self,other):
        print('{}想和{}交朋友'.format(self.name,other.name))
sanfeng = Man('张三丰','男',149,'白胡子')
sanfeng.name = '三丰'
print(sanfeng.huzi)
print(sanfeng.name)
sanfeng.eat()
damo = Man('达摩','男',148,'没有')
sanfeng.makeFriendWithOtherPeople(damo)