# 通过代码充分理解分支和函数

from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take? -- 这个房间全是金子，你要带多少钱？"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, you're not greedy, you win! -- 伙计，你不贪心，你赢了！")
    
    if how_much < 50:
        print "Nice, you're not greedy, you win! -- 很好，你不是很贪心，你赢了！"
        exit(0)
    else:
        dead("You greedy bastard! -- 你真是贪得无厌！")

# 选择左边房门执行函数
def bear_room():
    print "There is a bear here. -- 这里有一只熊。"
    print "The bear has a bunch of honey. -- 这只熊有一罐蜂蜜。"
    print "The fat bear is in front of another door. -- 那只胖熊在另一扇门前。"
    print "How are you going to move the bear? -- 你会怎样让熊离开哪里？"
    # 默认熊没有移动
    bear_moved = False

    while True:
        next = raw_input("> ")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off. -- 熊看着你，然后打你的脸。")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now. -- 熊离开了门，现在你可以通过他。"
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off. -- 熊生气了，咬断了你的腿。")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means. -- 我不知道什么意思。"

# 选择右边房门执行函数
def cthulhu_room():
    print "Here you see the great evil Cthulhu. -- 在这里你看到了一个伟大的恶鬼Cthulhu"
    print "He, it, whatever stares at you and you to insane. -- 他或者它无论什么盯着你，你都会疯掉。"
    print "Do you flee for your life or eat your head? -- 你是逃命还是让他吃了你的头？"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty! -- 非常美味！")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job! -- 非常好！"
    exit(0)

def start():
    print "You are in ad dark room. -- 你在一个黑房间里边"
    print "There is a door to your right and left. -- 你的左边和右边都有房门。"
    print "Which one do you take? -- 你怎么选择？"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve. -- 你在房间里转来转去，直到饿死。")

# 运行 start 函数
start()

# 主要练习分支流程的跳转判断
# 以及函数的相互调用执行