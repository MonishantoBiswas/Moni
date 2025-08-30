import cv2
import numpy as np
import face_recognition

img_andre_marie= face_recognition.load_image_file('ImagesBasics/andre-marie.jfif')
img_andre_marie=cv2.cvtColor(img_andre_marie,cv2.COLOR_BGR2RGB)

imgElon= face_recognition.load_image_file('ImagesBasics/elon mask.jfif')
imgElon=cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)


imgelontest= face_recognition.load_image_file('ImagesBasics/elon test.jfif')
imgelontest=cv2.cvtColor(imgelontest,cv2.COLOR_BGR2RGB)

faceloc= face_recognition.face_locations(imgElon) [0]
EncodeElon= face_recognition.face_encodings(imgElon) [0]
cv2.rectangle(imgElon, (faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),( 255,0,255),2)


cv2.imshow('Elon Mask',imgElon)
cv2.imshow('Andre Marie',img_andre_marie)
cv2.imshow('Elon Test',imgelontest)

canny_output= cv2.Canny(imgelontest,80,100)
cv2.imshow('canny',canny_output)
cv2.waitKey(0)