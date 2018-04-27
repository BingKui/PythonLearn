# 现在可以通过 if 和 else 来改变脚本的执行过程，改变执行分支

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s id probably better. Bear runs away." % bear
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries"
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
else:
    print "You stumnble around and fall on a knife and die. Good job!"


# 通过用户的输入来判断 进入那个流程分支 然后执行相应分支的代码 最后输出结果
# 通过两次的用户输入 来判断进入何种的流程，也可以在流程中继续添加，加深输入的步骤