# 引入需要的库
from PIL import Image, ImageDraw, ImageFont
def add_text(img, name, position):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('MFJingYue.ttf', 50)
    color = "#333333"
    draw.text(position, unicode(name, 'UTF-8'), font, fill=color)