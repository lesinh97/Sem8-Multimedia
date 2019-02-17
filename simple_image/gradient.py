import matplotlib.pylab as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage import filters

im = rgb2gray(imread('demo1.jpg')) # RGB image to gray scale
plt.gray()
plt.figure(figsize=(40,20))
plt.subplot(221)
plt.imshow(im)
plt.title('original', size=20)
plt.subplot(222)
edges_x = filters.sobel_h(im) 
plt.imshow(edges_x)
plt.title('sobel_x', size=20)
plt.subplot(223)
edges_y = filters.sobel_v(im)
plt.imshow(edges_y)
plt.title('sobel_y', size=20)
plt.subplot(224)
edges = filters.sobel(im)
plt.hist(edges)
plt.title('histogram_sobel', size=20)
plt.show()