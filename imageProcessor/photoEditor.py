from PIL import Image, ImageFilter
import os

path = './img'
pathOut = './editedImg'

for filename in os.listdir(path):
    img = Image.open(f'{path}/{filename}')

    edit = img.filter(ImageFilter.SHARPEN).convert('L') 
    cleanName = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{cleanName}_edited.jpg', 'JPEG')    