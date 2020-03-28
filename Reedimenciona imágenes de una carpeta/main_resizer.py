#!/usr/bin/env python3
from PIL import Image
import glob, os, shutil
from os import path
size = 128, 128
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

if os.path.isdir(d + '/data'):
  for infile in glob.glob(d + '/data/*.png'):
    print(infile)
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    new_im = im.rotate(0)
    new_im.save(file + ".jpeg", 'JPEG')
    print('Done!')
else:
  print('La carpeta no existe')