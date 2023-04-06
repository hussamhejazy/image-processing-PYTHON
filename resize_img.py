import cv2
 

def resize(img , scale_percent):
    
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)

    dim = (width, height)
    
    # Nearest neighbour interpolation
    near_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    # Bilinear interpolation
    bilinear_img = cv2.resize(img,dim, interpolation = cv2.INTER_LINEAR)
 
    cv2.imshow("Resized image", near_img)



if __name__ == '__main__':
    img = cv2.imread('../zCgel.jpg')
    size = int(input("Enter size to be applied to the image : "))
    resize(img,size)
    
