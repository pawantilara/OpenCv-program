import cv2
import numpy as np

img=cv2.imread('bookpage.jpg')
retval5,threshold5=cv2.threshold(img,225,255,cv2.THRESH_TRUNC)
retval1,threshold1=cv2.threshold(img,10,255,cv2.THRESH_BINARY)
'''First argument is the source image, which should be a grayscale image.
Second argument is the threshold value which is used to classify the pixel values.
Third argument is themaxVal which represents the value to
be given if pixel value is more than (sometimes less than) the threshold value.'''

'''openCV provides different styles of thresholding and it is decided by the fourth parameter
of the function. Different types are:

    cv.THRESH_BINARY
    cv.THRESH_BINARY_INV
    cv.THRESH_TRUNC
    cv.THRESH_TOZERO
    cv.THRESH_TOZERO_INV
    '''

grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)

gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv2.THRESH_BINARY,115,1)
gaus1=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_MEAN_C ,
                           cv2.THRESH_BINARY,115,1)
#gaus1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
'''
Adaptive Thresholding

In the previous section, we used a global value as threshold value.
But it may not be good in all the conditions where image has different lighting conditions in different
areas. In that case, we go for adaptive thresholding. In this, the algorithm calculate the threshold
for a small regions of the image. So we get different thresholds for
different regions of the same image and it gives us better results for images with varying illumination.
'''


'''
It has three ‘special’ input params and only one output argument.

Adaptive Method - It decides how thresholding value is calculated.

    cv.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
    cv.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where
    weights are a gaussian window.

Block Size - It decides the size of neighbourhood area.

C - It is just a constant which is subtracted from the mean or weighted mean calculated.
retval2,outsu=cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
'''

cv2.imshow('image',img)
cv2.imshow('Threshold5',threshold5)
cv2.imshow('Threshold1',threshold1)
#cv2.imshow('grayscaled',grayscaled)
cv2.imshow('gaus',gaus)
cv2.imshow('gaus1',gaus1)
#cv2.imshow('otsu',outsu)



cv2.waitKey(0)
cv2.destroyAllWindows()
