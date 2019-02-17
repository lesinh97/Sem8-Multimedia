import numpy as np
import cv2
# Load an color image in RGB mode
img = cv2.imread('demo1.jpg',255)
# show image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()