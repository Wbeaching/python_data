

# object祖类或者超类
# 子类能够继承父类的的属性和方法
class People(object):
    def __init__(self,name ,sex ,age):
         self.name = name
         self.sex = sex
         self.age = age
    def eat(self):
         print('活着的目的是为了吃')
    def makefriendwithpeople(self,other):
        print('我想和{}交朋友'.format(other.name))
class Man(People):
    def __init__(self,name ='',sex ='',age ='',huzi=''):
        # 继承父类的属性
        super(Man,self).__init__(name,sex,age)
        self.huzi = huzi
# 重写父类的名字
    def eat(self):
        super(Man,self).eat()
        print('我张三丰饿死也不吃你们一口饭')
sanfeng = Man('张三丰','男',149,'白胡子')
print(sanfeng.name)
sanfeng.name = '三丰'
print(sanfeng.huzi)
sanfeng.eat()
damo = Man('达摩','男',148,'没有')
sanfeng.makefriendwithpeople(damo)


# 一女子择偶，两个男士被选择
# 1.如果两男存款少于1000000都不考虑
# 2.如果两男存款大于10000000 跟存款多的走
# 3.男士
# 4.选择个子高的
# 5.如果身高都大于170 且相差不到5cm 看颜值（0,10）
# 6.低于7分的直接pass 高于7分选择颜值高的，如果相差不到2，看房子
# 7.房子不能低于100平且价值不能少于200万 如果都的话，选择价值高的
# 价值相差不多，看车子
# 8.车子价值不能少于50万 相差不到100万 抛硬币










