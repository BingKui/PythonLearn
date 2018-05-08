# python 是一门面向对象编程语言（OOP）想要很好的深入python，需要对面向对象编程有一定的了解

# 模块

# 1.模组是包含函数和变量的 python 文件
# 2.你可以 import 这个文件
# 3.然后你可以通过 ‘.’ 操作符访问模组中的函数和变量

# test.py
def apple():
    print "Apple is apple!"

txt = "This is a string!"

# 调用
import test

test.apple()
print test.txt

# 相比较，都是键值对的存在，只是调用方式不同

# python 中通用的模式
# 1.拿一个类似 key=value 风格的数据容易
# 2.通过 key 的名称来获取其中 value 的值

# 类

# 定义一个类
class MyClass(object):
    def __init__(self):
        self.txt = "This is a String!"

    def apple(self):
        print "Apple is apple!"


# 对象

# 对象相当于迷你版的 import

# 实例化一个类
thing = MyClass()

thing.apple()
print thing.txt


# 类的例子

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            pring line
    
happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
"With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


# 创建类时需要添加变量可以在 __init__ 方法中 self 后继续添加参数