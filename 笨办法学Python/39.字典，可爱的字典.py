# 字典既是容器，是一个对象可以存放 键值对
# 可以通过制定键值对 来给字典添加值
# 通过 del 关键字 来删除字典里边的数据（键值对）

class Song(object):
    def __init__(self, lyrice):
        self.lyrice = lyrice
    
    def sing_me_a_song(self):
        for line in self.lyrice:
            print line
    
happu_body = Song([
    'Happy birthday to you',
    "i don't want to get sued",
    "So I'll stop right there"
])

bulls_on_parade = Song([
    "They rally around the family",
    "With pockets full of shells"
])

happu_body.sing_me_a_song()

bulls_on_parade.sing_me_a_song()