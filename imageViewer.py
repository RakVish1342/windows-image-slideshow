from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ExifTags
import glob
import math
import os
import textwrap

# Replace path with image location
# Example: "C:\Users\tmp\images" becomes "C:\\Users\\tmp\\images"  
path = "./images"


globFileType = "*.jpg"
os.chdir(path)
for file in glob.glob(globFileType):
    print('------')
    print("Viewing file: ", file)
    img = Image.open(file)
    imgWidth, imgHeight = img.size
    # print(imgWidth, imgHeight)
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    if('XPComment' in exif):
        comment = exif['XPComment'].decode('utf-16-le').split('\x00')[0] # OR just use .decode('utf-16')
        print("Comment: ", comment)
        addCommentBar = True
    else:
        addCommentBar = False

    
    '''
    No Comment Bar to be added
    '''
    if(not addCommentBar):
        img.show()

    else:
        '''
        Comment Bar Settings
        '''

        # Font Settings 1
        font = ImageFont.truetype('arial.ttf', size=70)
        # Some sample test text for character width. Use of words compacts text, so less than 40 per character is used
        # w, h = font.getsize("D ") 
        # print("Character width and height ", w, h)

        # Comment Bar height
        margin = offset = charWidth = 40 # 40 = Approximate/max size of a character
        scale = 1.3 # Since characters together as words usually take less space, add some buffer space
        ctr = 0.3
        for line in textwrap.wrap(comment, width=scale*imgWidth/charWidth):
            offset += font.getsize(line)[1]
            ctr += 1

        charHeight = 94
        cmtBar = Image.new('RGBA', (imgWidth + 10, math.ceil(imgHeight + charHeight*ctr)), 'black')
        border = 5
        cmtBar.paste(img, (border,border,imgWidth+border, imgHeight+border))

        # Font Settings 2
        draw = ImageDraw.Draw(cmtBar)
        color = 'rgb(255, 255, 255)'

        # Text Wrapping
        margin = offset = charWidth = 40 # 40 = Approximate/max size of a character
        scale = 1.3 # Since characters together as words usually take less space, add some buffer space
        for line in textwrap.wrap(comment, width=scale*imgWidth/charWidth):
            draw.text((margin, imgHeight+offset), line, font=font, fill=color)
            offset += font.getsize(line)[1]


        '''
        Display Image
        '''
        cmtBar.show()


    '''
    User Input
    '''
    cmd = input("Give me a command: Press 'q' to quit. Press 'n' for the next image. ")
    # print("CMD::: ", ord(cmd), cmd)
    cmd = ord(cmd)
    while (1):
        if(cmd == 81 or cmd == 113): # Q=81 or q=113
            exitFlag = True
            break
        elif(cmd == 78 or cmd == 110): # N=78 or n=110
            cmtBar.close()
            exitFlag = False
            break
        else:
            cmd = input("Invalid Option. Press 'q' to quit. Press 'n' for the next image. ")
            cmd = ord(cmd)
            continue

    if(exitFlag):
        break

print('------')
print("Done viewing all images in the folder :)")
print('------')
