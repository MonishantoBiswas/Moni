
import cv2
import numpy as np
cap = cv2.VideoCapture("message1.mp4")
#Inside the parenthesis we can change the value of the subtractor.
# History is the number of the last frame that are taken into consideretion (by default 120).
#The threshold value is the value used when computing the difference to extract the background.
# A lower threshold will find more differences with the advantage of a more noisy image.
#Detectshadows is a function of the algorythm that can remove the shadows if enabled.
#There are no right or wrong values, you need to try different settings to see what best fits your need.
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=10, detectShadows=True)
while True:
    _, frame = cap.read()
    mask = subtractor.apply(frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(30)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()