import cv2
import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data, color, exposure

filename = r"demo1.jpg"

im = cv2.imread(filename)

gr = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 

print(im.shape)
image = gr

fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualise=True)

fig, ax = plt.subplots(1, 2, figsize=(20, 10), sharex=True, sharey=True)

ax[0].axis('off')
ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Input image')
ax[0].set_adjustable('box-forced')

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))

ax[1].axis('off')
ax[1].imshow(hog_image, cmap=plt.cm.gray)
ax[1].set_title('Histogram of Oriented Gradients')
ax[1].set_adjustable('box-forced')

plt.show()