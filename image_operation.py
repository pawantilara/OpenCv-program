import cv2
import numpy as np

img=cv2.imread('first.jpg',cv2.IMREAD_COLOR)
img[55,55]=[255,255,255]
px=img[55,55]
#roi=img[100:150,100:150]#roi-region of image//ie pixels
#print(roi)
img[100:150,100:150]=[25,25,255]


watch_face=img[37:150,107:250]


img[0:113,0:143]=watch_face



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



