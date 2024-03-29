import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    lower_yellow = np.array([100,60,60])
    upper_yellow = np.array([200,220,220])

    mask = cv2.inRange(frame,lower_yellow,upper_yellow)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    blur = cv2.GaussianBlur(res,(15,15),0)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('blur',blur)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()