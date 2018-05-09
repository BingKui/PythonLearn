# 大部分使用继承的场合都可以使用合成来代替，尽量避免多级继承

# 继承

# 继承的用处，就是用来指明一个类的大部分或全部功能，都从一个父类中获得

# 写法
# class Foo(Bar):

# 上面的代码就是继承：Foo 继承 Bar

# 这么做，父类和子类有三种交互方式
# 1.子类上的动作完全等同于父类上的动作
# 2.子类上的动作完全改写父类上的动作
# 3.子类上的动作部分变更了父类上的动作

# 隐式继承

class Parent(object):
    def implicit(self):
        print "Parent implicit"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# 显式覆写

class ParentTwo(object):
    def override(self):
        print "ParentTwo override()"
    
class ChildTwo(ParentTwo):
    def override(self):
        print "ChildTwo override()"

dadTwo = ParentTwo()
sonTwo = ChildTwo()

dadTwo.override()
sonTwo.override()

# 在运行前或运行后覆写

class ParentThree(object):
    def altered(self):
        print "ParentThree altered()"

class ChildThree(ParentThree):
    def altered(self):
        print "ChildThree before altered()"
        super(ChildThree, self).altered()
        print "ChildThree after altered()"

dadThree = ParentThree()
sonThree = ChildThree()

dadThree.altered()
sonThree.altered()

# 一起使用三种方式

class ParentFour(object):
    def override(self):
        print "Parent override()"
    
    def implicit(self):
        print "Parent implicit()"
    
    def altered(self):
        print "Parent altered()"

class ChildFour(ParentFour):
    def override(self):
        print "ChildeFour override()"

    def altered(self):
        print "ChildFour befor altered()"
        super(ChildFour, self).altered()
        print "ChildFour after altered()"

dadFour = ParentFour()
sonFour = ChildFour()

dadFour.implicit()
sonFour.implicit()

dadFour.override()
sonFour.override()

dadFour.altered()
sonFour.altered()

# 多重继承
# class SuperFun(Child, BadStuff):
    # pass


# 合成

class Other(object):
    def override(self):
        print "Ohter override()"
    
    def implicit(self):
        print "Other implicit()"
    
    def altered(self):
        print "Other altered()"
    
class OtherChild(object):
    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print "OtherChild override()"
    
    def altered(self):
        print "OtherChild before altered()"
        self.other.altered()
        print "OtherChild after altered()"

otherSon = OtherChild()

otherSon.implicit()
otherSon.override()
otherSon.altered()

# 继承和合成的应用场景

# 继承能够很好的增加代码的重复利用率，避免到处都是一样的代码

# 使用建议
# 1.不惜一切代价的避免多重继承，多重继承带来的麻烦比能解决的问题多
# 2.如果一些代码会在不同位置的和场合应用到，金陵合成把它们做成模块
# 3.只有在代码之间有清晰的关联，可以通过一个单独的共性练联系起来的时候再使用继承

