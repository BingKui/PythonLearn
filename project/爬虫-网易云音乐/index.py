#!/usr/bin/python
# -*- coding: utf-8 -*-
# 目标：爬取网易云音乐播放数大于1000W的歌单
from selenium import webdriver

# 定义网易云音乐的歌单第一个 url
url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'

# 用 PhantomJS 接口创建一个 Selenium 的 WebDriver
driver = webdriver.PhantomJS()

# 解析每一页，知道下一页为空
while url != 'javascript:void(0)':
    # 用 WebDriver 加载页面
    driver.get(url)
    # 切换到内容的 iframe
    driver.switch_to.frame("contentFrame")
    # 定位歌单标签
    res = driver.find_element_by_id("m-pl-container").find_element_by_tag_name("li")
    # 解析每一页中的所有歌单
    for i in range(35):
        # 获取播放次数
        times = res[i].find_element_class_name("nb").text
        if '万' in times and int(times.split("万")[0]) > 1000:
            # 获取封面
            picture = res[i].find_element_class_name("j-flag").get_attribute('src')
            # 获取链接
            link = res[i].find_element_class_name("tit").get_attribute('href')
            # 名字
            name = res[i].find_element_class_name("tit").text
            # 作者
            author = res[i].find_element_class_name("nm").text
            # 输出爬取到的数据
            print("名字：%s 作者：%s") % (name, author)
    # 定位下一页
    url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')



# 代码已不可用，由于 Selenium 与 PhantomJS 的分家