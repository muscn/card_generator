#!/usr/bin/env python

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from urllib import urlretrieve
import os

# The co-ordinates
devil_number_xy = (614, 68)
name_xy = (433, 438)
phone_xy = (643, 521)
qr_xy = (65, 302)

# The font-sizes
devil_number_size = 58
name_size = 60
phone_size = 19

draw_qr = False

# Sample Data
pk = 7
name = u'Amrit Bahadur Khanal Chhetri'
phone = u'98x11x3333'
devil_number = u'007'


# Pre-processing
name = name.upper()
names = name.split()
last_name = names[-1]
names_sans_last = names[0:-1]
if len(names_sans_last) > 1:
    middle_names = names_sans_last[1:]
    # multiple middle names support :D
    middle_name_initials_list = [middle_name[0]+'.' for middle_name in middle_names]
    middle_name_initials = ' '.join(middle_name_initials_list)
    name_sans_last = names_sans_last[0] + ' ' + middle_name_initials + ' '
else:
    name_sans_last = names_sans_last[0] + ' '

img = Image.open('watermarked.jpg')
# img = Image.open('watermarked_with_qr.jpg')
# img = Image.open('front.jpg')

draw = ImageDraw.Draw(img)
# write devil number
font = ImageFont.truetype(os.path.join('fonts', 'Aileron-ThinItalic.otf'),
                          devil_number_size)
draw.text(devil_number_xy, '#' + devil_number, (255, 255, 255), font=font)

# write first (and middle, if any) name
font = ImageFont.truetype(os.path.join('fonts', 'Aileron-Regular.otf'),
                          name_size)
draw.text(name_xy, name_sans_last, (255, 255, 255), font=font)
# write phone number
font = ImageFont.truetype(os.path.join('fonts', 'Aileron-Regular.otf'),
                          phone_size)
draw.text(phone_xy, phone, (255, 255, 255), font=font)


if draw_qr:
    # download qr
    if not os.path.exists('qrs'):
        os.makedirs('qrs')
    urlretrieve(
                'http://api.qrserver.com/v1/create-qr-code/?data=http://manutd.org.np/' + devil_number + '&size=160x160&ecc=H&color=ffffff&bgcolor=000',
                os.path.join('qrs', str(pk) + '.png'))
    qr = Image.open(os.path.join('qrs', str(pk) + '.png'))
    #make qr transparent
    qr = qr.convert('RGBA')
    data = qr.getdata()
    new_data = []
    for item in data:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    qr.putdata(new_data)
    qr.save(os.path.join('qrs', str(pk) + '.png'))
    # write qr to image
    img = img.convert('RGBA')
    img.paste(qr, qr_xy, qr)

if not os.path.exists('sample_cards'):
    os.makedirs('sample_cards')
img.save(os.path.join('sample_cards', str(pk) + '.jpg'))
