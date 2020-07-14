from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ExifTags
import glob
import math
import os

# Replace path with image location
# Example: "C:\Users\tmp\images" becomes "C:\\Users\\tmp\\images"  
path = "./images"


globFileType = "*.jpg"
os.chdir(path)
for file in glob.glob(globFileType):
    print("Viewing file: ", file)
    img = Image.open(file)
    width, height = img.size
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    comment = exif['XPComment'].decode('utf-16-le').split('\x00')[0] # OR just use .decode('utf-16')
    print(comment)
    # img.show()

    cmtBar = Image.new('RGBA', (width+10, math.ceil(height+height/5)), 'black')
    border = 5
    cmtBar.paste(img, (border,border,width+border, height+border))
    
    draw = ImageDraw.Draw(cmtBar)
    font = ImageFont.truetype('arial.ttf', size=70)
    location = (0, height)
    color = 'rgb(255, 255, 255)' # black color
    draw.text(location, comment, fill=color, font=font)
    w, h = font.getsize(comment)

    cmtBar.show()
