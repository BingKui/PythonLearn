# append 工作原理（arr.append('111')）
# 1.找到 arr 这个变量，查看 arr 是个什么类型的变量
# 2.执行 . 运算符，查看支持的函数方法
# 3.对比是否存在 append 的方法，存在则查看是否需要参数
# 4.填入参数执行 append 方法，对 arr 进行添加子元素操作

# 创建一个状态到缩写的对象
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
# 创建一个存在一些城市的set集合
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# 添加一些城市
cities['NY'] = 'New York'
cities['OR'] = 'Portlan'

# 打印一些城市
print '-' * 10
print "NY State has:", cities['NY']
print "OR State has:", cities['OR']

# 打印一些州
print '-' * 10
print "Michigan's abbreviation is:", states['Michigan']
print "Florida's abbrebiation is:", states['Florida']

# 使用城市字典
print '-' * 10
print "Michigan has:", cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]

# 打印每个州的缩写
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# 打印每个城市的州
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the citu %s" % (abbrev, city)

# 同时打印两个
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# 安全的得到一个可能不存在的值
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# 通过默认值获取一个城市
city = cities.get('TX', 'Doed Not Exist')
print "The city for the state 'TX' is: %s" % city

