# 类

class TheThing(object):
    def __init__(self):
        self.number = 0
    
    def some_function(self):
        print "I got called."

    def add_me_up(self, more):
        self.number += more
        return self.number

# 两件不同的事情

a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print b.add_me_up(30)

print a.number
print b.number


# 研究一下，这个就是参数传递的方法
# 从一个类到另一个类 你可能需要这些
# 注意 class 的缩进 
# 注意冒号的用法
# 理解 self 在 __init__ 等函数中的用法及概念


# __dict__:存储对象的一些属性