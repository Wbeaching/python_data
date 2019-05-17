
# python 里面容器的类型有几种
# list
# tuple
# set
# dict
# list 里面的元素是可变的
# tuple里面的元素是不变的，只能查看 不能曾删改
tp1 = ()
tp1 = tuple()
tp1 = ((),[],{},1,2,3,'a','b','c',3.14,True)
print(tp1[:])
print(tp1[1::2])
print(tp1[5])
# AttributeError: 'tuple' object has no attribute 'remove'
# attribute 属性 object 对象
# 属性错误：元祖属性没有属性'remove'
# tp1.remove(1)
# 作业：重现8种错误





























