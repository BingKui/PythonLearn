# 接收参数的脚本

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first varialbe is:", first
print "Your second varialbe is:", second
print "Your third varialbe is:", third

# 运行命令:python 13.参数、解包、变量.py first 2nd 3rd

# 传入过多或者过少参数都会报错
