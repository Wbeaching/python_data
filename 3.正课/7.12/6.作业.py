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
# # def
# class People(object):
#     def __init__(self,name='' ,sex='',height='',money='',yanzhi='',house_area='',house_value='',car_value=''):
#         self.name = name
#         self.sex = sex
#         self.height = height
#         self.money = money
#         self.yanzhi = yanzhi
#         self.house_area = house_area
#         self.house_value = house_value
#         self.car_value = car_value
#     def sexIsFit(self,other1,other2):
#         if self.sex == False and self.sex==other1.sex==other2:
#             print('咱仨有意思吗')
#             return False
#         if other1.money ==other2.money<1000000:
#             print('凉凉')
#             return False
# class Man1(People):
#     def __init__(self):
#         super(Man1,self).__init__(name='' ,sex='',height='',money='',yanzhi='',house_area='',house_value='',car_value='')
#     def makefriend(self,other1,other2):
#
#
#
#
#
#
#
# class Man2(People):
#     def __init__(self):
#         super(Man2, self).__init__(name='', sex='', height='', money='', yanzhi='', house_area='', house_value='',car_value='')
#
