# 可以通过在函数中添加提示，来提示用户输入两个值

age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight?")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)