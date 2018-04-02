# 变量
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# 加分题
# 使用浮点数，得到的结果也是浮点数
# 了解每一行最主要的意思
# 变量在使用之前需要先进行定义
# = 是赋值语句（equal）
# 空格一般使用 _ 表示，来区分单词，保证变量有意义，易于理解
# 变量名，尽量使用有意义的单词作为变量，多个单词中间使用_进行分割，保证可读性

# 常见问题
# 1. = 和 == 的区别？
# Ans：= 是赋值语句，把右边的值赋给左边的变量
#      == 是检查语句，检查左右两边的值是否相等
# 2. 写成x=100而非x = 100是否一样可以？
# Ans： 一样，只是不推荐写，左右两边加上空格易于代码阅读
