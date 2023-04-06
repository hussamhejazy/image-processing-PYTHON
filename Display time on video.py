import cv2
import datetime

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Display the time on video
    font = cv2.FONT_HERSHEY_SIMPLEX
    datet = str(datetime.datetime.now())
    ret = cv2.putText(frame, datet, (10, 50), font, 1,
                      (0,255,255),2,cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow("video",ret)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

