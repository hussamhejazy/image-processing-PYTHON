#solve problem 3.13 using python

import cv2
import numpy as np
from matplotlib import pyplot as plt


img_f = cv2.imread('4.2.01.tiff' )
img_f = cv2.cvtColor(img_f, cv2.COLOR_BGR2RGB)
img_g = cv2.imread('4.2.04.tiff' )
img_g = cv2.cvtColor(img_g, cv2.COLOR_BGR2RGB)

a = img_f + img_g
b = img_f - img_g
c = img_f * img_g
d = img_f / img_g
titles = ['f','g','f+g' , 'f-g', 'f*g', 'f/g']
images = [img_f,img_g ,a , b, c ,d]
#display images after applying operations to them
for i in range(6):
    plt.subplot(2 , 3 , i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

#Display histogram of images after applying operations to them
for i in range(4):
    plt.subplot(1 , 4 , i+1)
    plt.hist(images[i].ravel(),255,[0,255])
    plt.title(titles[i])

plt.show()


