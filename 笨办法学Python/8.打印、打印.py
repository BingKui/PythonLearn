# 直接上代码，不废话
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ('one', "tow", 'three', "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# %r 输出的字符串默认是已 '' 包裹的，如果字符创中存在 ‘ 则为 "" 包裹。

# 进阶
print "中文打印测试：%r" % "这个是打印的中文"
print "中文打印测试：%s" % "这个是打印的中文"