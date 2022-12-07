import cv2
import numpy

img= cv2.imread("poster.jpg")

rocket=img[120:360,400:500]

img[0:240,500:600]= rocket

# text_to_show="Hello World!!!!"
cv2.putText(img,"Hello Shriyansh",(20,200),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=2,color=(255,0,0))

cv2.imshow("output",img)

cv2.waitKey(0)