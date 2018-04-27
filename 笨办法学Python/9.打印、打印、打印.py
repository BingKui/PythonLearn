# 转移字符的加入

days = "Mon Tue Wed Thu Fri Sat Sun"
# 换行符的使用
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months:", months

# 多行打印
print """
There's sonmething going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

# 进阶
# 使用%r 输出 months
print "月份：%r" % months

# + 用来拼接连个字符串为一个  , 用来区分不同的参数

print "Aaaaa" + "baaaaa" # 输出一个字符串
print "Aaaaa", "baaaaa" # 输出两个字符串