# 引入需要的库
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import pathlib
import requests
import qrcode

def add_text(img, text, size, position, color="#9400D3"):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('MFJingYue.ttf', size)
    draw.text(position, text, fill=color, font=font, align="center")

# 获取每行第一个字的横坐标
# 根据字体大小处理
# 每行最多14个字
def get_x_position(len):
    max = 14
    x = 50 + (max - len) * 25 / 2
    return x
# 生成二维码
def make_qrcode(url, type):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=3
    )
    qr.add_data(url)
    # qr.make(fit = True)
    img = qr.make_image()
    img = img.convert("RGBA")
    icon = None
    if type == 'netease':
        icon = Image.open(pathlib.Path('netease.png'))
    elif type == 'qq':
        icon = Image.open(pathlib.Path('qq.png'))
    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w/factor)
    size_h = int(img_h/factor)
    
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    
    w = int((img_w-icon_w)/2)
    h = int((img_h-icon_h)/2)
    img.paste(icon, (w,h), icon)
    return img

def merge_img(img_src, name, count, address, author, type):
    save_name = './' + name + '.jpg'
    name = unicode(name, 'UTF-8')
    count = unicode("播放量：" + count, 'UTF-8')
    author = unicode("创建人：" + author, 'UTF-8')
    background_img = Image.open(pathlib.Path('background.jpg'))
    # 获取远程图片
    response = requests.get(img_src)
    img = Image.open(BytesIO(response.content))
    # 设置图片替换位置
    box = (100, 50, 350, 300)
    # 选取图片
    region = img
    region = region.resize((box[2] - box[0], box[3] - box[1]))
    # 粘贴到背景图上
    background_img.paste(region, box)
    # 添加名字
    name_len = len(name)
    if name_len <= 14:
        x = get_x_position(name_len)
        add_text(background_img, name, 25, (x, 330))
    else:
        name_one = name[0:14]
        print name_one
        add_text(background_img, name_one, 25, (50, 330))
        name_two = name[14:name_len]
        print name_two
        x = get_x_position(len(name_two))
        add_text(background_img, name_two, 25, (x, 370))
    # 添加创建者
    add_text(background_img, author, 20, (50, 560), color='white')
    # 添加播放数
    add_text(background_img, count, 20, (50, 600), color='white')
    # 生成二维码地址
    qrcode_img = make_qrcode(address, type)
    # 粘贴到背景图上
    box_qrcode = (300, 527, 425, 652)
    print qrcode_img.size, qrcode_img.mode
    # qrcode_img.save('./qrcode.png')
    region_qrcode = qrcode_img
    region_qrcode = region_qrcode.resize((box_qrcode[2] - box_qrcode[0], box_qrcode[3] - box_qrcode[1]))
    background_img.paste(region_qrcode, box_qrcode)
    # 保存图片
    background_img.save(save_name)

img_one = 'https://p.qpic.cn/music_cover/1Fr9IFMhWDPeUzWKVEjn3VLzce1PenAOaaImqzoibx2iaE5rhV0RwMYA/300?n=1'
img_two = 'http://p1.music.126.net/wpahk9cQCDtdzJPE52EzJQ==/109951163271025942.jpg?param=140y140'
address_one = 'https://y.qq.com/n/yqq/playsquare/2643652402.html#stat=y_new.playlist.pic_click'
address_two = 'https://music.163.com/#/playlist?id=2201879658'
name_one = '回头率最高的50首手机铃声'
name_two = '你的青春里有没有属于你的一首歌？'
merge_img(img_one, name_one, '4622.8万', address_one, author="Harry", type="qq")
merge_img(img_two, name_two, '2428万', address_two, author="mayuko然", type="netease")