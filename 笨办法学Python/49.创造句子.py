# 一个句子的组成由：主语 + 谓语 + 宾语

# 匹配和窥视

# 要达到这个效果需要
# 1.循环访问元组列表的方法
# 2.匹配主谓宾设置不同种类元组的方法
# 3.一个 ”窥视“ 潜在元组的方法
# 4.跳过我们不在乎的内容的方法

# parser.py
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        math(word_list,word_type)

# 句子的语法

# 流程大概如下：
# 1.使用 peek 识别下一个词
# 2.如果单词和我们的语法匹配，调用函数处理语法
# 3.如果语法不匹配，就抛出一个错误
# 4.全部分析完后，得到一个语句对象，然后应用到游戏中就行了

class ParseError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, object):
        # 记住我们去（‘名词’，‘公主’）的元组转换它们
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParseError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParseError("Expected a noun or diredtion next.")

def parse_subject(word_list, subj):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)

def parse_sentence(word_list):
    skip(word_list, 'stop')

    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        # 假设主体是玩家
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParseError("Must start with subject, object, or verb not: %s" % start)



# 异常
# 定义异常函数
# 怎么抛出异常

