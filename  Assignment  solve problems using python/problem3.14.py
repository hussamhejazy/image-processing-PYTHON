#solve problem 3.14 using python

import cv2
import numpy as np
from matplotlib import pyplot as plt

#plt.subplot(121)
img_a = np.zeros((8,8))
img_a[1::2 , 0::2] = 255
img_a[0::2 , 1::2] = 255
print(img_a)
blur_a = cv2.blur(img_a,(3,3))
plt.xticks([])
plt.yticks([])
#plt.title('image (a)')
#plt.imshow(img_a , cmap='binary')


#plt.subplot(122)
img_b = np.zeros((8,8))
img_b[0::1 , 4::1] = 255
img_b[4::1 , 3::7] = 0
blur_b = cv2.blur(img_a,(3,3))
plt.xticks([])
plt.yticks([])
#plt.title('image (b)')
#plt.imshow(img_b , cmap='binary')
#plt.show()

#histogram for image (a) and(b)
#Note : the histogram is similar for each of the two pictures
plt.subplot(121)
plt.hist(img_a.ravel(),255,[0,255])
plt.title('Histogram image (a)')

plt.subplot(122)
plt.hist(img_b.ravel(),255,[0,255])
plt.title('Histogram image (b)')

plt.show()

#histogram for image (a) and(b) after bluring
#Note : After blurring, the histogram for each image is different
plt.subplot(121)
plt.hist(blur_a.ravel(),255,[0,255])
plt.title('(a) after bluring')

plt.subplot(122)
plt.hist(blur_b.ravel(),255,[0,255])
plt.title('(b) after bluring')

plt.show()

#plt.imshow(blur , cmap='binary')
#plt.show()
