
class People(object):
    # 实例方法在创建的时候需要一个self参数
    # 表示调用该方法的对象是谁
    def instanceFun(self):
        print('我是一个实力方法')
        # 类方法 在创建的时候需要一个cls 参数
        # 表示调用该方法的类是谁
    @classmethod
    def classFun(cls):
        print('我是一个类方法')
    # 静态方法
    # 静态该方法无需指明调用的对象
    @staticmethod
    def staticFun():
        print('我是一个静态方法')


        # 实例方法 类方法和静态方法的使用场景
        # 如果想让方法根据调用的对象的不同，显示不同的内容
        # 或者实现功能的不同，经常使用对象方法
        # 2.如果方法不需要做上述操作，方法不需要根据调用的对象
        # 的不同

# 创建一个实例对象
# 对象方法也叫实例方法
p =People()
p.instanceFun()
# 类方法要使用类名+方法名字的的方法来调用
People.classFun()
# 静态方法可以通过类名/对象+方法名字的方法来调用
print(People.instanceFun())
People.staticFun()
p.staticFun()

















