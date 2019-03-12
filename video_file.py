import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
'''FourCC is a 4-byte code used to specify the video codec
 In Fedora: DIVX,XVID, MJPG, X264, WMV1, WMV2.
 (XVID is more preferable. MJPG results in high size video.
 X264 gives very small size video) •
 In Windows: DIVX (More to be tested and added)

 '''
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:
    ret ,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
       
    
