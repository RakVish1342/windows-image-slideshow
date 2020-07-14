from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ExifTags
import glob
import os

# Add another backslash before each backslash in the path copied.
path = "C:\\Users\\Vish\\Desktop\\gmk\\comments"


globFileType = "*.jpg"
os.chdir(path)
for file in glob.glob(globFileType):
    print("Viewing file: ", file)
    img = Image.open(file)
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    comment = exif['XPComment'].decode('utf-16-le').split('\x00')[0] # OR just use .decode('utf-16')
    print(comment)


    # img.show()

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype('arial.ttf', size=70)
    (x, y) = (50, 50)
    color = 'rgb(0, 0, 0)' # black color
    draw.text((x, y), comment, fill=color, font=font)


    img.show()
