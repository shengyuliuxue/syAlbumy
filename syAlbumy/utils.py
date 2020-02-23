#usr/bin/env/python3
#-*- coding:utf-8 -*-
import os
import PIL
from PIL import Image
from flask import current_app

def resize_image(filename, path, base_width):

    img = Image.open(path)
    filename, ext = os.path.splitext(filename)
    if img.size[0] <= base_width:
        return filename + ext
    w_percent = (base_width / float(img.size[0]))
    h_size = int(float(img.size[1]) * float(w_percent))

    img = img.resize((base_width, h_size), PIL.Image.NEAREST)

    filename += current_app.config['ALBUMY_PHOTO_SUFFIX'][base_width] + ext
    img.save(os.path.join(current_app.config['ALBUMY_UPLOAD_PATH'], filename),
             optimize=True, quality=85)
    return filename
