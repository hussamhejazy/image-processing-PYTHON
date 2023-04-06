#solve problem 3.21 using python

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('5.1.13.tiff')
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

# cv2.blur ..... Averaging
blur_a = cv2.blur(img,(23,23))
blur_b = cv2.blur(img,(25,25))
blur_c = cv2.blur(img,(45,45))

titles = ['image' , 'mask 23' , 'mask 25' , 'mask 45']
images = [img , blur_a ,blur_b , blur_c]

#display images 
for i in range(4):
    plt.subplot(2 , 2 , i+1)
    plt.imshow(images[i] , 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()









 
