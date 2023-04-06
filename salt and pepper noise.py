
import numpy as np
import random
import cv2
def salt(image,number):
    rows,cols=image.shape
    saltImage=np.copy(image)
    
    for i in range(number):
        randR=random.randint(0,rows-1)
        randC=random.randint(0,cols-1)
        saltImage[randR][randC]=255
    return saltImage
 
if __name__=="__main__":
    img=cv2.imread("5.1.09.tiff",cv2.IMREAD_GRAYSCALE)
    simg=salt(img,100)
    cv2.imshow("raw",img)
    cv2.imshow("salt",simg)
    cv2.waitKey()
    cv2.destroyAllWindows()
