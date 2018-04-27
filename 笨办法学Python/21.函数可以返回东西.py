# 通过return返回值来设置变量的值

def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtract %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiply %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Divide %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(15, 20)
height = subtract(78, 1)
weight = multiply(90, 3)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# 一个额外的训练表达式

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes:", what, "Can you do it by hand?"
