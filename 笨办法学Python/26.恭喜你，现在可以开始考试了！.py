# 教程的前半部分基本完成，前半部分主要是用来了解基础知识，一些方法的基础用法
# 后半部分会将了解到逻辑判断，能够通过简单的逻辑判断添加实现有用的功能

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# 少了个冒号：
def print_first_word(words)
    """Prints the first word after popping it off."""
    word = words.poop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    # 少了个右括号
    word = words.pop(-1
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

# 这个结果根本不是5是6
five = 10 - 2 + 3 - 5
# 应该使用%d
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    # 因该是 / 而不是 \
    jars = jelly_beans \ 1000 
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# 应该是start_point 不是 start-point
beans, jars, crates == secret_formula(start-point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
# 少了个右括号
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont


sentence = "All good things come to those who weight."
# 在同一个文件总存在这个方法 不用使用ex25前缀
words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
# 函数执行前边不能有点号
.print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
prin sorted_words

print_irst_and_last(sentence)
# 不能有缩进
   print_first_a_last_sorted(senence)


# 修改上边的代码，代码中有错误，错误已通过注释给出