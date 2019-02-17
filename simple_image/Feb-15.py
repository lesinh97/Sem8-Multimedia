import numpy as np
import cv2
# gradient
from skimage.io import imread
from skimage.color import rgb2gray
from skimage import filters

# importing library for plotting 
from matplotlib import pyplot as plt

# Load an color image in RGB mode
img = cv2.imread('demo1.jpg',255)
# show image

# convert to gray
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# histogram
# find frequency of pixels in range 0-255 
histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
# show the plotting graph of an image 
plt.plot(histr) 
plt.show() 


plt.gray()
plt.figure(figsize=(20,20))
plt.subplot(221)
plt.imshow(img_gray)
plt.title('original', size=20)
plt.subplot(222)
edges_x = filters.sobel_h(img_gray)
plt.imshow(edges_x)
plt.title('sobel_x', size=20)
plt.imshow(histr)
plt.title('histogram sobel_x', size=20)
plt.subplot(222)
plt.subplot(223)
edges_y = filters.sobel_v(img_gray)
plt.imshow(edges_y)
plt.title('sobel_y', size=20)
plt.subplot(224)
edges = filters.sobel(img_gray)
plt.imshow(edges)
plt.title('sobel', size=20)
plt.show()

cv2.imshow('Original', img)
cv2.imshow('Gray', img_gray)
cv2.waitKey(0)
