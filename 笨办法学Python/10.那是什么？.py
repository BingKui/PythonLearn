# 转移序列 \

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# 转移序列 列表
# \\ 反斜杠
# \' 单引号
# \" 双引号
# \a 响铃符
# \b 退格符
# \f 换页符
# \n 换行符
# \r 回车符
# \t Tab制表符
# \N{name} Unicode 数据 库中的字符名， 其中 name 就是它的名字
# \uxxxx 值为 16 位十 六进制值 xxxx 的字符
# \Uxxxxxxxx 值为 32 位十 六进制值 xxxx 的字符
# \v 垂直制表符
# \ooo 值为八进制ooo的字符
# \xhh 值为十六进制数hh的字符

# 测试运行--加载中的图标
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,