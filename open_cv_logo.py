import cv2
import numpy as np

def create_blank(width, height, color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in BGR"""
    image = np.zeros((height, width, 3), np.uint8)
    # Fill image with color
    image[:] = color

    return image


def draw_half_circle_rounded(image):
    height, width = image.shape[0:2]
    # Ellipse parameters
    radius = 100
    center = (width / 2, height - 25)
    axes = (radius, radius)
    angle = 0
    startAngle = 180
    endAngle = 360
    thickness = 10

    # http://docs.opencv.org/modules/core/doc/drawing_functions.html#ellipse
    #cv2.ellipse(image, center, axes, angle, startAngle, endAngle, 255, thickness)
    #image = cv2.ellipse(image,(width/2,height-25),(100,100),0,180,360,255,10)
    image = cv2.ellipse(image,(width/2,height-25),(100,100),0,180,360,255,10)


# Create new blank 300x150 white image
width, height = 300, 150
image = create_blank(width, height, color=(255,255,255))
cv2.imshow('image',image)
draw_half_circle_rounded(image)
cv2.imwrite('half_circle_rounded.jpg', image)
