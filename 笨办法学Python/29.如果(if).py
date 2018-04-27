# 判断语句，主要用来判断改变流程

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not Many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

# if 用来判断后边紧跟的表达式的布尔值是否是True，如果为True则执行后续代码块
# 紧跟的底部代码需要缩进