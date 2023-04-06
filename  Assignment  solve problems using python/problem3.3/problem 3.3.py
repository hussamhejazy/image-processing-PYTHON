#solve problem 3.3 using python

import cv2
import numpy as np
from matplotlib import pyplot as plt

#When r < m, the slope is increasing.
#When r > m, the slope is decreasing.
#When r = m, the slope is infinite and s = (Normalized).
'''
The continuous function for implementing the required contrast stretching
transformation including parameter E For controlling the slope of the function
as it transitions from low to high gray-level values is,
'''
# s ... output image , r ... input image
L = 256
m = L/2
#E For controlling the slope of the function
E = 5
r  = cv2.imread('5.1.12.tiff')

#The continuous function
s = 1 / (1 + ((m/r)**E))


titles = ['input image','output image']
images = [r,s]
#Display input and outbut image
for i in range(2):
    plt.subplot(1 , 2 , i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

