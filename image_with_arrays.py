import numpy as np
import cv2

black = np.zeros([600,600])
black[0:100,500:600]=255
black[200:400,200:400]= 56

print(black)

cv2.imshow("black",black)

cv2.waitKey(0)