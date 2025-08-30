import cv2
import time

cap= cv2.VideoCapture('F:/EEE/EEE BOOKS/EEE Books -41/Thesis 4000/video/hello2.mp4')


fps= int(cap.get(cv2.CAP_PROP_FPS))

print("This is the fps ", fps)

if cap.isOpened() == False:
    print("Error File Not Found")

while cap.isOpened():
    ret,frame= cap.read()

    if ret == True:

        time.sleep(1/fps)

        cv2.imshow('frame', frame)

        if cv2.waitKey(27) & 0xFF == ord('q'):
            break

    else:
        break


cap.release()
cv2.destroyAllWindows()

