# 通过 if 和 else 来完成不同分支流程执行不同的任务

people = 20
cars = 30
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < prople:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

# 可以通过不同的 if 、 else 和 elif 完成多分支的逻辑判断处理