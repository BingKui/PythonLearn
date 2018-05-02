# 接下来学习如何创建列表 list 
# 然后通过循环输出列表中的所有值

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same ad above
for fruit in fruits:
    print "A Fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we hava to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list。" % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

# rang 函数的范围为 前后都不包括 相当于 1 <= x < 10 等价于 x in range(1, 10) 等价于 x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
