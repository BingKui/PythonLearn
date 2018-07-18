#!/usr/bin/python
# -*- coding: utf-8 -*-
# 引入需要的库
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import pathlib
import urllib2
import requests

base_img = Image.open(pathlib.Path('1.png'))
url = 'https://p.qpic.cn/music_cover/gaSSCRswoq7NlpHA8vK1PqGr6rCVbibywq9UsT7ZEeT1Ur5oFmibzWhA/300?n=1'
# req = urllib2.Request(url)
# html = urllib2.urlopen(req, timeout=10)
# img = html.read()
response = requests.get(url)
link_img = Image.open(BytesIO(response.content))
# 可以查看图片的 size 和 mode
print link_img.size, link_img.mode
# 底图上需要 p 掉的区域
box = (166, 64, 320, 337)

# 加载需要合成的图片
tmp_img = Image.open(pathlib.Path('2.png'))
# 这里选择一块区域或者整张图片
# 选取整整图片
region = tmp_img

region = region.resize((box[2] - box[0], box[3] - box[1]))
base_img.paste(region, box)

# 使用自定义字体
font = ImageFont.truetype('MFJingYue.ttf', 50);

draw = ImageDraw.Draw(base_img)
# 防止乱码，做 Unicode 处理
draw.text((0, 0), unicode('康兵奎!','UTF-8'), '#333333', font)

base_img.save('./out.png')
