# if 语句的规则
# 1.每一个 if 语句，必须包含一个 else
# 2.如果一个 else 永远都不应该被直行到，必须在 else 语句后边使用一个叫 die 的函数。
# 3. if 语句的嵌套尽量不要超过两层， 最好保持在一层
# 4.将 if 语句当做段落来对待
# 5.布尔测试必须简单，如果复杂需要把运算放在变量中进行运算

# 根据实际情况，寻找合适的规则是正确的方法，不一定要完全使用上边的规则

# 循环使用的规则
# 1.只有在循环永不停止的情况下使用 while-loop 
# 2.普通类型的循环都使用 for-loop 尤其是在循环的对象数固定或者有限的情况下

# _arr = [1, 2, 3, 4, 5]
# for i in _arr:
#     print i

# 调试小技巧
# 1.不要使用 “debugger”。因为输出信息大部分没用，只会增加调试难度。
# 2.最好是使用 print 打印出每一步的结果，然后查看哪里出错了。
# 3.注释一部分代码，一段一段代码的执行，知道找出出错的代码。

# 实例
# 游戏名：逃离城堡
# 规则：按照提示输入相应的选择，答对进入下一步，城堡分三层，每层有3个关卡，全部通过逃离城堡
# 思路：
# 创建问题库，随机抽出问题，回答正确则通过，失败损失生命，生命结束游戏结束


# 引入需要的包

import random

# 题库
topics = ["苹果的英文单词（全部小写）是什么？", "什么人整天吃个没完没了呢？", "4+4+4+4（猜一种水果）", "微软的创始人是谁？", "香蕉的英文单词（全部小写）是什么？", "100 - 10 - 2 =", "orange是什么水果？", "三天一共有多少个小时？", "一个小时有多少秒？", "中国国土面积有多少平方公里？", "", "1 + 1 ="]
answer = ["apple", "口吃的人", "石榴", "比尔盖茨", "banana", "88", "橘子", "72", "3600", "9634057", "2", "2"]

# 定义血量
hp = 3
# 定义楼层
floor = 3
# 定义进度，进度等于 3 时 楼层减一层，等于等于零时 回答正确步骤加 1， 回答错误 楼层加一层 并重置步骤为2
step = 1

# 剔除重复问题
old_index = []

# 输入提示图标
propmt = ">>> "

def game_over(tip):
    print tip, "游戏结束，重新开始输入（restart），关闭输入（over）"
    next = raw_input(propmt)
    global floor
    global hp
    global step
    if next == "restart":
        floor = 3
        hp = 3
        step = 1
        start()
    elif next == "over":
        exit(0)
    else:
        print "不能理解你输入的是什么，请按照提示输入！"

# 生成一个0-11的随机整数
def random_index():
    global old_index
    _ran = random.randint(0, 11)
    if _ran in old_index:
        return random_index()
    else:
        old_index.append(_ran)
        return _ran


# 判断答案是否正确，并进行下一步操作
def check_answer(index, input):
    global answer
    print "你的答案为：%s" % input
    print "正确答案为：", answer[index]
    print "答案是否正确：", answer[index] == input
    control_floor_and_step(input == answer[index])

# 判断当前的进度和楼层，控制游戏的结束和开始
def control_floor_and_step(flag):
    global hp
    if flag:
        # 回答正确，步骤进1
        control_step(True)
    else:
        # 回答错误，步骤退1，血量减1
        control_step(False)
        print "回答错误，生命值下降"
        hp -= 1
    check_game()

# 控制步骤
def control_step(add_step):
    global step
    if add_step and step < 3:
        print "关卡加1"
        step += 1
    elif step == 3:
        control_floor(True)
        step = 1
    elif step == 0:
        control_floor(False)
        step = 2
    else:
        print "关卡减1"
        step -= 1

# 控制楼层
def control_floor(add_floor):
    global floor
    if add_floor and floor <= 3:
        print "楼层减1"
        floor -= 1
    elif floor == 3:
        print "你回到了起点！"
    else:
        print "楼层加1"
        floor += 1

# 检查当前游戏，是否是已经结束
def check_game():
    global floor
    global hp
    if floor == 0:
        game_over("你赢了！")
    if hp == 0:
        game_over("你输了！")
    # 没有输也没有赢，继续进行
    start()

def start():
    print "-------------------------------------------------------"
    print "当前楼层：%d, 当前关卡：%d, 当前生命值：%d" % (floor, step, hp)
    # 获取一个随机数，然后获取题库中相应的题目和答案
    index = random_index()
    print "请回答问题：", topics[index]

    next = raw_input(propmt)
    
    check_answer(index, next)

# 实例
# 游戏名：逃离城堡
# 规则：按照提示输入相应的选择，答对进入下一步，城堡分三层，每层有3个关卡，全部通过逃离城堡
# 思路：
# 创建问题库，随机抽出问题，回答正确则通过，失败损失生命，生命结束游戏结束
print "                                       "
print "                  /\                   "
print "                 /  \                  "
print "                /    \                 "
print "               /      \                "
print "       △      / ------ \      △        "
print "       |     /          \     |        "
print "      / \   /            \   / \       "
print "     /   \ /--------------\ /   \      "
print "    /-----\                /-----\     "
print "    |     |  □ ________ □  |     |     "
print "    |  □  |   |        |   |  □  |     "
print "    |     |   |        |   |     |     "
print "    |     |   |        |   |     |     "
print " ------------------------------------- "
print "                                       "
print "              逃 离 城 堡               "
print "                                       "
print "游戏背景："
print "你被关在了一个城堡中，你要通过自己的知识，回答问题逃离出去！知识就是力量，开始吧！！！"
print "游戏规则："
print "1.城堡分 3 层，每层有 3 个关卡，你拥有 3 次失败重来的机会。"
print "2.回答正确进入下一关卡。每过 3 个关卡，进入下一层。"
print "3.回答错误，退回上个关卡，损失一点生命值，生命值为0，则游戏失败。"
print "4.在每层的第一个关卡的时候，回答错误，有一次答题机会，如果回答错误，楼层加 1 ，成功保留当前楼层，进入第一个关卡。"
start()