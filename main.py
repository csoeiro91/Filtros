import cv2
import numpy as np


img = cv2.imread("C:/batman.jpg",cv2.IMREAD_COLOR)

# Copy the thresholded image.
floodfill = img.copy()

# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = img.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)


seed        = (430,273)
colorToFill = (0,0,150)
minColor    = (0,0,0)
maxColor    = (23,23,23)

# Floodfill from point (0, 0)
cv2.floodFill(floodfill, mask, seed, colorToFill,minColor, maxColor)


#cv2.imshow('Mask', mask)
cv2.imshow('Original', img)
cv2.imshow('floodfill',floodfill)

cv2.waitKey()

cv2.destroyAllWindows()