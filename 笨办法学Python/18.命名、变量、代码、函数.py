# 函数的编写
# 函数可以做三件事情：
# 1.它们给代码片段命名，就像变量给字符串和数字命名一样
# 2.它们可以接受参数，就像脚本接受argv一样
# 3.通过使用前两个，它们可以让你创建”微型脚本“或者”小命令“

# this one is link your script with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin."

print_two('one', 'two')
print_two_again('three', 'four')
print_one('five')
print_none()

# 使用def命令定义函数，紧接着是函数名，然后参数使用()来包裹才能正常工作，然后以冒号:结束
# 下一行缩进开始，是属于函数的内容

# 函数名称规则：
# 函数名以字母和数字以及下划线组成，不能以数字开始就可以