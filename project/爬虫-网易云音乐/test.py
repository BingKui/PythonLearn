# 引入网络库中的 urlopen 方法
from urllib import urlopen
# 引入安装的 beautifulsoup 对象
from bs4 import BeautifulSoup

# 打开 url 获取页面内容
html = urlopen('http://jr.jd.com')
# HTML 对象传入 beautifulsoup 对象
bs_obj = BeautifulSoup(html.read(), 'html.parser')
# 找到需要读取的对象
text_list = bs_obj.find_all("a", "nav-item-primary")
# 循环打印读取的文本
for text in text_list:
    print(text.get_text())
# 关闭页面的获取
html.close()