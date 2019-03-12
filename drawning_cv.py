import cv2
import numpy as np

img=cv2.imread('first.jpg',cv2.IMREAD_COLOR)


#img = cv2.medianBlur(img,5)

cv2.line(img,(0,0),(150,150),(255,255,255),15)
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
cv2.circle(img,(100,63),55,(0,0,255),-1)
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#cv2.ploylines(img,[pts],True,(0,255,255),5)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tus!',(0,130),font,1,(20,25,25),5,cv2.LINE_AA)
img = cv2.ellipse(img,(125,225),(100,50),0,0,360,255,3)


pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
print(pts)
pts = pts.reshape((-1,1,2))
print(pts)
img = cv2.polylines(img,[pts],True,(0,255,255))


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
