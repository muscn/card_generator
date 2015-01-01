#!/usr/bin/env python

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from urllib import urlretrieve
import os
import re

# The co-ordinates
devil_number_ending_xy = (744, 68)
name_ending_xy = (1010, 438)
phone_ending_xy = (1010, 520)
qr_xy = (65, 393)

# The font-sizes
devil_number_size = 58
name_size = 60
phone_size = 43

draw_qr = True
# possible values: L, M, Q, H
qr_error_correction = 'M'

# Sample Data
pk = 7
name = u'Shaswot Adhikari'
phone = u'9876543211'
devil_number = u'007'

# Pre-process the name
name = name.upper()
names = name.split()
last_name = names[-1]
names_sans_last = names[0:-1]
if len(names_sans_last) > 1:
    middle_names = names_sans_last[1:]
    # multiple middle names support - Amrit Bahadur Khanal Kshetri :D
    middle_name_initials_list = [middle_name[0]+'.' for middle_name in middle_names]
    middle_name_initials = '  '.join(middle_name_initials_list)
    name_sans_last = names_sans_last[0] + '  ' + middle_name_initials + ' '
else:
    name_sans_last = names_sans_last[0] + ' '

# Pre-process the phone number
phone_code = None
pattern = '^([0|\\+[0-9]{1,5})?[-\s]?([7-9][0-9]{9})$'
matches = re.search(pattern, phone)
if matches:
    phone_code = matches.groups()[0]
    phone = matches.groups()[1]
    if phone_code:
        phone_code = phone_code.strip('\n\t\r\+\-')
        phone_code = phone_code.lstrip('00')
    else:
        phone_code = '977'
    phone_code = '+' + phone_code + '  '


img = Image.open('watermarked.jpg')
# img = Image.open('watermarked_with_qr.jpg')
# img = Image.open('front.jpg')

draw = ImageDraw.Draw(img)

# write devil number
devil_number_font = ImageFont.truetype(os.path.join('fonts', 'Aileron-ThinItalic.otf'),
                                       devil_number_size)
devil_number_text_size = draw.textsize('#' + devil_number, font=devil_number_font)
devil_number_xy = (devil_number_ending_xy[0] - devil_number_text_size[0], devil_number_ending_xy[1])
draw.text(devil_number_xy, '#' + devil_number, (255, 255, 255), font=devil_number_font)

# write name
name_sans_last_font = ImageFont.truetype(os.path.join('fonts', 'Aileron-ThinItalic.otf'), name_size)
name_sans_last_size = draw.textsize(name_sans_last, font=name_sans_last_font)
last_name_font = ImageFont.truetype(os.path.join('fonts', 'Aileron-Italic.otf'), name_size)
last_name_size = draw.textsize(last_name, last_name_font)
name_length = name_sans_last_size[0] + last_name_size[0]
name_xy = (name_ending_xy[0] - name_length, name_ending_xy[1])
last_name_xy = (name_xy[0] + name_sans_last_size[0], name_xy[1])
draw.text(name_xy, name_sans_last, (255, 255, 255), font=name_sans_last_font)
draw.text(last_name_xy, last_name, (255, 255, 255), font=last_name_font)



# write phone number
phone_font = ImageFont.truetype(os.path.join('fonts', 'Aileron-Italic.otf'),
                                     phone_size)
phone_font_size = draw.textsize(phone, phone_font)
phone_xy = (phone_ending_xy[0] - phone_font_size[0], phone_ending_xy[1])
draw.text(phone_xy, phone, (255, 255, 255), font=phone_font)
if phone_code:
    phone_code_font = ImageFont.truetype(os.path.join('fonts', 'Aileron-ThinItalic.otf'),
                                         phone_size)
    phone_code_size = draw.textsize(phone_code, phone_code_font)
    phone_code_xy = (phone_xy[0] - phone_code_size[0], phone_ending_xy[1])
    draw.text(phone_code_xy, phone_code, (255, 255, 255), font=phone_code_font)



if draw_qr:
    # download qr
    if not os.path.exists('qrs'):
        os.makedirs('qrs')
    urlretrieve(
                'http://api.qrserver.com/v1/create-qr-code/?data=http://manutd.org.np/' + devil_number + '&size=208x208&ecc=' + qr_error_correction + '&color=ffffff&bgcolor=000',
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
