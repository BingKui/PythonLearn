# 格式化字符串， 包含变量内容的字符串
my_name = 'KangBingKui'
my_age = 25
my_height = 174
my_weight = 160
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "基础用法"
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s heir." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d. " % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# 所有的格式化字符
# %%：百分号标记，输出一个%
# %c：字符传及其ASCII码
# %s：字符串
# %d：有符号整数（十进制） 
# %u：无符号整数（十进制）
# %o：无符号整数（八进制）
# %x：无符号整数（十六进制）
# %X：无符号整数（十六进制大写字符）
# %e：浮点数字（科学计数法）
# %E：浮点数字（科学计数法，用E代替e）
# %f：浮点数字（用小数点符号）
# %g：浮点数字（根据值的大小采用%e或%f）
# %G：浮点数字（类似于%g）
# %p：指针（用十六进制打印指的内存地址）
# %n：存储输出字符的数量放进参数列表的下一个变量中

# 进阶
print "进阶用法"
# 指定字段的最小宽度
new_year = 2018
new_month = 4
new_day = 21
print "%4d-%02d-%02d" % (new_year, new_month, new_day)
# 保留精度
fValue = 9.12345
print "%08.3f" % fValue # 保留宽度为8的3位小数浮点型
# 十进制
print "%d" % 10
# 八进制
print "%o" % 10 
# 十六进制，空缺补0
print "%02x" % 10
print "%04X" % 10
# 科学计数法输出浮点型保留2位小数
print "%.2e" % 1.2999