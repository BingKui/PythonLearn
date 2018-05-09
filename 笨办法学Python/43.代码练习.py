# 代码练习

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
PHRASES = {
    "class ###(###):": "Make a class named ### that is-a ###.",
    "class ### (object): \n\t def __init__(self, ***)": "class ### has-a __init__ that takes self and *** parameters.",
    "class ###(object): \n\t def ***(self, @@@)": "class ### has-a function named *** that takes self and @@@ parameters.",
    "*** = ###()": "Set *** to an instance of class ###.",
    "***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}

# 练习短语
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# 从网站上下载单词
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

# 代码缺失  不是完整示例  暂停 进行下一章学习