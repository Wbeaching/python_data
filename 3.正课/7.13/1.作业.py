#
# # 一女子择偶，两个男士被选择
# # 1.如果两男存款少于1000000都不考虑
# # 2.如果两男存款大于10000000 跟存款多的走
# # 3.男士
# # 4.选择个子高的
# # 5.如果身高都大于170 且相差不到5cm 看颜值（0,10）
# # 6.低于7分的直接pass 高于7分选择颜值高的，如果相差不到2，看房子
# # 7.房子不能低于100平且价值不能少于200万 如果都有的话，选择价值高的
# # 价值相差不多，看车子
# # 8.车子价值不能少于50万 相差不到10万 抛硬币
# # 使用继承
# # 传入两个对象
# # def 抛硬币
# class people(object):
#     def __init__(self,name='' ,sex='',money='',heigit='',face='',house_area='',house_value='',car_value='',win = ''):
#          self.name = name
#          self.sex = sex
#          self.money = money
#          self.heigit = heigit
#          self.face = face
#          self.house_area = house_area
#          self.house_value = house_value
#          self.car_value = car_value
#          self.win = win
# class woman(people):
#     def ishaswin(self ,man1,man2):
#         if man1.win ==False and man2.win ==False:
#             return False
#         else:
#             return True
#     def choiceboyfriendwithboy(self,xiaowang,xiaoli):
#         if xiaowang.money<1000000 and xiaoli.money<100000:
#             print('俩人都钱少')
#             return
#         elif xiaowang.money<1000000 and xiaoli.money>=1000000:
#             print('小李胜出')
#             return
#         elif xiaowang.money>=1000000 and xiaoli.money <1000000:
#             print('小王胜出')
#             return
#         elif xiaowang.money>=10000000 and xiaoli.money<10000000:
#             print('小王胜出')
#             return
#         elif xiaowang.money<=10000000 and xiaoli.money<10000000:
#             print('小李胜出')
#             return
#
#
#
#
#
#
#
#
#
#
# class man(people):
#     def __init__(self,name ,sex,money,heigit,face,house_area,house_value,car_value,win ):
#         super(man,self).__init__(self,name ,sex,money,heigit,face,house_area,house_value,car_value,win )
# xiaomei = woman()
# xiaowang = man('小王',True,10000000,169,7,100,200,50,False)
# xiaoli = man('小李',True,100000,180,10.50,80,20,False)
# xiaomei.choiceboyfriendwithboy(xiaowang,xiaoli)
#
#
#
#
# 2.‘name=zhangsan,age=6,fond=xuexi’，请获取fond对应的值
def man(fond):
    return fond
print(man('xuexi'))
