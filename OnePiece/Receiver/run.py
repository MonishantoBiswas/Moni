import cv2
from threading import Thread
from receiver import receiver
from codes import unipolar
import time

def main() -> None:
    "Just read frame and feed to queue"
    instance = unipolar()
    object = receiver(callback=instance.manchester)
    cap = cv2.VideoCapture("demo5.mp4") # Live video feed here @ 1 (0 for moni)
    print("Camera Opened.")
    #time.sleep(3)
    print("Here we go...")
    """frame_width = 640
    frame_height = 480
    ROI_left = frame_width // 2 - 25
    ROI_right = frame_width // 2 + 25
    frame = cv2.imread("frameh.png")
    frame = cv2.resize(frame, (frame_width, frame_height)) # Resize
    frame = frame[:, ROI_left : ROI_right] # ROI Cropping
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    object.convert(gray_image)
    return"""

    thread1 = Thread(target=object.parallel, daemon=True)
    thread1.start()

    while cap.isOpened():
        ret, frame = cap.read()
        
        if ret == True:
            object.q.put(frame)
            if cv2.waitKey(27) & 0xFF == ord('q'): # Is this gonna slow us down?
                break
        else:
            break
    object.flag = True
    print("\nWaiting for daemon thread to join, Closing...")
    thread1.join()

if __name__ == "__main__":
    main()