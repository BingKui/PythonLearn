# 对象和类 其实是同样的东西，只是在不同的时间的叫法不同

# 对象属于一个类 而某个类又属于另一个类

# 练习
# 在 “## ??“ 处标注出是 “is-a” 还是 “has-a” 的关系

class Animal(object):
    pass

## ??
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name
        ## ??
        self.pet = None

## ??
class Employee(Person):
    def __init__(self, name, salary):
        ## ??
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(object):
    pass

## ??
class Halibut(object):
    pass

## ??
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")