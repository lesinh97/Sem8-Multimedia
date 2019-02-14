import cv2
import numpy as np
import matplotlib.pyplot as plt

def show(img):
    plt.imshow(img, cmap="gray")
    plt.show()

# load the input image
img = cv2.imread('demo1.jpg',0);
show(img)

ret, mask = cv2.threshold(img, 60, 120, cv2.THRESH_BINARY)  # turn 60, 120 for the best OCR results
kernel = np.ones((5,3),np.uint8)
mask = cv2.erode(mask,kernel,iterations = 1)
show(mask)

# I used a version of OpenCV with Tesseract, you may use your pytesseract and set the modes as:
#   OCR Enginer Mode (OEM) = 3 (defualt = 3)
#   Page Segmentation mode (PSmode) = 11 (defualt = 3)
tesser = cv2.text.OCRTesseract_create('test/','eng','0123456789',11,3)
retval = tesser.run(mask, 0) # return string type

print ('OCR:' + retval)