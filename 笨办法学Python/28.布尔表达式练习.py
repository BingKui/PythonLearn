# 逻辑关系的组合就是布尔表达式

# 布尔表达式基本练习
# True and True  --> True
# False and True  --> False
# 1 == 1 and 2 == 1  --> False
# "test" == "test"  --> True
# 1 == 1 or 2 != 1  --> True
# True and 1 == 1  --> True
# False and 0 != 0  --> False
# True or 1 == 1  --> True
# "test" == "testing"  --> False
# 1 != 0 and 2 == 1  --> False
# "test" != "testing"  --> True
# "test" == 1  --> False
# not (True and False)  --> True
# not (1 == 1 and 0 != 1)  --> False
# not (10 == 1 or 100 == 1000)  --> True
# not (1 != 10 or 3 == 4)  --> False
# not ("testing" == "testing" and "Zed" == "Cool Guy")  --> True
# 1 == 1 and not ("testing" == 1 or 1 == 0)  --> True
# "chunke" == "bacon" and not (3 == 4 or 3 == 3)  --> False
# 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")  --> False

# 运行一下查看一下结果是否正确

print 'True and True -->', True and True
print 'False and True -->', False and True
print '1 == 1 and 2 == 1 -->', 1 == 1 and 2 == 1
print '"test" == "test" -->', "test" == "test"
print '1 == 1 or 2 != 1 -->', 1 == 1 or 2 != 1
print 'True and 1 == 1 -->', True and 1 == 1
print 'False and 0 != 0 -->', False and 0 != 0
print 'True or 1 == 1 -->', True or 1 == 1
print '"test" == "testing" -->', "test" == "testing"
print '1 != 0 and 2 == 1 -->', 1 != 0 and 2 == 1
print '"test" != "testing" -->', "test" != "testing"
print '"test" == 1 -->', "test" == 1
print 'not (True and False) -->', not (True and False)
print 'not (1 == 1 and 0 != 1) -->', not (1 == 1 and 0 != 1)
print 'not (10 == 1 or 100 == 1000) -->', not (10 == 1 or 100 == 1000)
print 'not (1 != 10 or 3 == 4) -->', not (1 != 10 or 3 == 4)
print 'not ("testing" == "testing" and "Zed" == "Cool Guy") -->', not ("testing" == "testing" and "Zed" == "Cool Guy")
print '1 == 1 and not ("testing" == 1 or 1 == 0) -->', 1 == 1 and not ("testing" == 1 or 1 == 0)
print '"chunke" == "bacon" and not (3 == 4 or 3 == 3) -->', "chunke" == "bacon" and not (3 == 4 or 3 == 3)
print '3 == 3 and not ("testing" == "testing" or "Python" == "Fun") -->', 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")

# 布尔值判断的简单流程
# 1.找到相等判断的部分（== or !=），将结果改写成最终值（True 或 False）
# 2.找到括号里的 and/or，先计算出它们的值
# 3.找到每一个 not，算出它们反过来的值
# 4.找到剩下的 and/or，解出它们的值
# 5.做完这些，就是简单的 True 和 False 的判断了

# 其它字符操作的结果
# "test" and "test"  --> "test"
# 1 and 1 --> 1