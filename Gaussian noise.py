
import cv2
import numpy as np
 
img = cv2.imread('5.1.09.tiff')
# Generate Gaussian noise
gauss = np.random.normal(0,1,img.size)
gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')

# Add the Gaussian noise to the image
img_gauss = cv2.add(img,gauss)

# Display the image
cv2.imshow('image',img_gauss)
