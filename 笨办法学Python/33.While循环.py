# while-loop 循环：一直执行代码，知道判断条件为 False 才停止
# 可以用来做循环任务

# 使用建议
# 1.尽量少用 while-loop ，大部分时候使用 for-loop 是更好的选择
# 2.重复检查 while 语句， 确定测试布尔表达式 最终会变成 False 
# 3.如果不确定，就在 while-loop 的结尾打印测试值， 看看结果

i = 0
numbers = []
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print " At the bottom i is %d" % i

print "The numbers:"

for num in numbers:
    print num