# 字符串，使用''或者""包裹的字符，中间可以使用格式化字符
x = 'There are %d types of people.' % 10
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those eho %s." % (binary, do_not)
# 原始值
print x
print y
# %r 与 %s 比较
print "I said: %r" % x
print "I also said: '%s'." % y

#输出内容可以定义为变量，然后进行输出
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

# 字符之间可以通过 + 来进行拼接
w = "This is the left side of..."
e = "a string with a right side."
print w + e

# 进阶
# %r 用来做debug比较好，应为输出的为原始值，便于查找问题
# 其他符号用来向用户显示输出