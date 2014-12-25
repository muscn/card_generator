#!/usr/bin/env python

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
# from urllib import urlretrieve
import os

# The co-ordinates
devil_number_xy = (613, 75)
name_xy = (433, 438)
phone_xy = (643, 521)
qr_xy = (65, 302)

# Sample Data
pk = 7
name = u'Shashwot Adhikari'
phone = u'98x11x3333'
devil_number = u'#007'

img = Image.open('watermarked_card.jpg')
draw = ImageDraw.Draw(img)
# write devil number
font = ImageFont.truetype(os.path.join('fonts', 'Aileron-ThinItalic.otf'), 19)
draw.text(devil_number_xy, devil_number, (255, 255, 255), font=font)
# write name
font = ImageFont.truetype(os.path.join('fonts', 'Aileron-Regular.otf'), 19)
draw.text(name_xy, name, (255, 255, 255), font=font)
# write phone number
font = ImageFont.truetype(os.path.join('fonts', 'Aileron-Regular.otf'), 19)
draw.text(phone_xy, phone, (255, 255, 255), font=font)

# download qr
# if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'qrs')):
# os.makedirs(os.path.join(settings.MEDIA_ROOT, 'qrs'))
# urlretrieve('http://api.qrserver.com/v1/create-qr-code/?data=http://manutd.org.np/007&size=160x160&ecc=H',
#             os.path.join(settings.MEDIA_ROOT, 'qrs', str(self.id) + '.png'))
# qr = Image.open(os.path.join(settings.MEDIA_ROOT, 'qrs', str(self.id) + '.png'))
# write qr to image
# draw.bitmap(qr_xy, qr)

if not os.path.exists('sample_cards'):
    os.makedirs('sample_cards')
img.save(os.path.join('sample_cards', str(pk) + '.jpg'))
