# 通过用户输入获取文件名 然后读取文件内容 打印出来

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

# 一个文件可以打开多次 而没有问题
