import cv2
import numpy as np

img1 = cv2.imread('C:/Users/97059/Desktop/image.jpg')
img2 = cv2.imread('C:/Users/97059/Desktop/image.jpg')
psnr = cv2.PSNR(img1, img2)

def calculate_psnr(img1, img2, max_value=255):
    """"Calculating peak signal-to-noise ratio (PSNR) between two images."""
    mse = np.mean((np.array(img1, dtype=np.float32) - np.array(img2, dtype=np.float32)) ** 2)
    if mse == 0:
        return 100
    return 20 * np.log10(max_value / (np.sqrt(mse)))

print(calculate_psnr(img1,img2,255))
