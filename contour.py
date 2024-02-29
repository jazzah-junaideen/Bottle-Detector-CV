import cv2
import numpy as np 
#from matplotlib import pyplot as plt 


framewidth = 640
frameHeight = 480

source = cv2.VideoCapture(1)
source.set(3,framewidth)
source.set(4,frameHeight)

while cv2.waitKey(1) != 27: # Escape key
    has_frame,frame = source.read()
    if not has_frame:
        break
    blurred_frame = cv2.GaussianBlur(frame,(7,7),1)
    gs_frame = cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Coutour Detection", gs_frame)

source.release()
cv2.destroyWindow("Coutour Detection")