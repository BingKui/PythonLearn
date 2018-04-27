# 接收输入 改变输入 打印改变后的输入
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weigh = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weigh)

# print 后边输入都好，print不会输出新行符而结束这一行跑到下一行

# 如果想把用户的输入转换格式可以  int(raw_input()) ==>装换成int()整数类型

