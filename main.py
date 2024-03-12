from PIL import ImageDraw,ImageFont,Image        # all libraries
import cv2
import numpy as np
import math
from functools import cache

fileName="Touhou - Bad Apple.mp4"   # input file name here
chars = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"   # ASCII characters
charlist=list(chars)
charlen=len(charlist)
interval=charlen/256
scale_factor=0.09
charwidth=10
charheight=10

@cache
def get_char(i):
    return charlist[math.floor(i*interval)]

cap=cv2.VideoCapture(fileName)        # Video capture

Font=ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf',15)    # font name

# ASCII Generator Code
while True:    
    _,img=cap.read()
    img=Image.fromarray(img)

    width,height=img.size
    img=img.resize((int(scale_factor*width),int(scale_factor*height*(charwidth/charheight))),Image.NEAREST)
    width,height=img.size
    pixel=img.load()
    outputImage=Image.new("RGB",(charwidth*width,charheight*height),color=(0,0,0))
    dest=ImageDraw.Draw(outputImage)
# Screen output
    for i in range(height):
        for j in range(width):
            r,g,b=pixel[j,i]
            h=int(0.299*r+0.587*g+0.114*b)
            pixel[j,i]=(h,h,h)
            dest.text((j*charwidth,i*charheight),get_char(h),font=Font,fill=(r,g,b))

    open_cv_image=np.array(outputImage)
    key=cv2.waitKey(1)        # exit VideoProcess press "q"
    if key == ord("q"):          
        break
    cv2.imshow("Bad Apple",open_cv_image)    # title= "Bad Apple"
# Auto end code
cap.release()
cv2.destroyAllWindows()