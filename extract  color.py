import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #define range color
    #red
    lower_red = np.array([161,155,84])
    upper_red = np.array([179,255,255])
    red_mask = cv2.inRange(hsv,lower_red,upper_red)
    #blue
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    blue_mask = cv2.inRange(hsv,lower_blue,upper_blue)
    #green
    lower_green = np.array([50,50,120])
    upper_green = np.array([70,255,255])
    green_mask = cv2.inRange(hsv,lower_green,upper_green)

    mask = red_mask + blue_mask + green_mask


    res = cv2.bitwise_and(frame,frame , mask = mask)

    # Display the resulting frame
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

