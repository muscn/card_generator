#!/usr/bin/env python

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
# from urllib import urlretrieve
import os


pk = 7
full_name = u'Shashwot Adhikari'
mobile = u'98x11x3333'
devil_number = u'#007'

img = Image.open('watermarked_card.jpg')
draw = ImageDraw.Draw(img)
# write devil number
font = ImageFont.truetype(os.path.join('fonts', 'Aileron-ThinItalic.otf'), 19)
draw.text((613, 75), devil_number, (255, 255, 255), font=font)
# write name
font = ImageFont.truetype(os.path.join('fonts', 'Aileron-Regular.otf'), 19)
draw.text((433, 438), full_name, (255, 255, 255), font=font)
# write phone number
font = ImageFont.truetype(os.path.join('fonts', 'Aileron-Regular.otf'), 19)
draw.text((643, 521), mobile, (255, 255, 255), font=font)

# download qr
# if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'qrs')):
# os.makedirs(os.path.join(settings.MEDIA_ROOT, 'qrs'))
# urlretrieve('http://api.qrserver.com/v1/create-qr-code/?data=http://manutd.org.np/007&size=160x160&ecc=H',
#             os.path.join(settings.MEDIA_ROOT, 'qrs', str(self.id) + '.png'))
# qr = Image.open(os.path.join(settings.MEDIA_ROOT, 'qrs', str(self.id) + '.png'))
# write qr to image
# draw.bitmap((65, 302), qr)

if not os.path.exists('sample_cards'):
    os.makedirs('sample_cards')
img.save(os.path.join('sample_cards', str(pk) + '.jpg'))
