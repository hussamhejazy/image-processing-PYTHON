import cv2
import numpy as np
from matplotlib import pyplot as plt
 

img = cv2.imread('4.2.07.tiff')
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

scale_percent = 500
    
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
    
# Nearest neighbour interpolation
near_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# Bilinear interpolation
bilinear_img = cv2.resize(img,dim, interpolation = cv2.INTER_LINEAR)
 


titles = ['original image' , 'Nearest neighbour' , 'Bilinear']
images = [img , near_img , bilinear_img]
    
#display images 
for i in range(3):
    plt.subplot(1 , 3 , i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
