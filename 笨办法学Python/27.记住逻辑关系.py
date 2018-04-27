# 到目前为止，已经了解了 读取文件、命令行处理以及基本的数学运算
# 现在开始学习逻辑代码的实现方式

# 逻辑术语

# 基本逻辑术语分类
# and 与
# or 或
# not 非
# != (not equal) 不等于
# == (equal) 等于
# >= (greater-than-equal) 大于等于
# <= (less-than-equal) 小于等于
# True 真
# False 假

# 基本逻辑真值表
#----------------------
# Not           True?
#----------------------
# not False     True
# not True      False

#-----------------------------
# OR                   True?
#-----------------------------
# True or False        True
# True or True         True
# False or True        True
# False or False       False

#-----------------------------
# AND                  True?
#-----------------------------
# True and False       False
# True and True        True
# False and True       False
# False and False      False

#-----------------------------
# NOT OR               True?
#-----------------------------
# not(True or False)   False
# not(True or True)    False
# not(False or True)   False
# not(False or False)  True

#-----------------------------
# NOT AND              True?
#-----------------------------
# not(True and False)  True
# not(True and True)   False
# not(False and True)  True
# not(False and False) True

#-----------------------------
# !=                   True？ 
#-----------------------------
# 1 != 0               True
# 1 != 1               False
# 0 != 1               True
# 0 != 0               False

#-----------------------------
# ==                   True?
#-----------------------------
# 1 == 0               False
# 1 == 1               True
# 0 == 1               False
# 0 == 0               True

# 这些就是python中的基本逻辑关系，记住这些对于代码的编写有很大帮助

# 基本逻辑关系可以理解为：
# or：只要有真就为真
# and：只要有假就为假
# not：取反操作