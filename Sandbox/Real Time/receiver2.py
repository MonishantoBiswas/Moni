# Assuming a byte will range over two frames only, the program can be simplified
# Also, every Byte must have a high (1) addressing bit
import cv2
from threading import Thread
from queue import Queue
from time import sleep

class receiver:
    def __init__(self) -> None:
        self.q = Queue()
        self.flag = False
        self.data = None # Frame containing information
        self.single, self.double = [26, 32], [56, 61] # lower and upper limit of strip heights
        self.shutter_loss = 7 # Pixel loss due to frame transitioning
    

    def isStriped(self, gray_image, brightness_threshold = 100) -> bool:
        "Check if a frame is striped"
        # Apply Canny edge detection
        edges = cv2.Canny(gray_image, threshold1=100, threshold2=200) # Calibrate here
        # For instance, you can calculate the average pixel intensity of bright and dark areas
        average_bright = gray_image[edges > 0].mean()

        ## Condition to declare: May be changed
        if average_bright < brightness_threshold:
            return True
        return False
    

    def transfer(self, h, type, loss=False) -> None:
        "Prints according to height"
        if self.single[0] <= h <= self.single[1]:
            print(type, end="")
        elif self.double[0] <= h <= self.double[1]:
            print(type * 2, end="")
        else:
            if not loss:
                self.transfer(h + self.shutter_loss, type, True)
        

    def convert(self) -> None:
        "Retrieves Binary data from B&W image"
        # Apply binary threshold to segment black strips
        _, binary_image = cv2.threshold(self.data, 80, 200, cv2.THRESH_BINARY_INV) # Calibrate here
        # Find contours in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        init = None
        for contour in reversed(contours):
            x, y, w, h = cv2.boundingRect(contour)
            if init:
                self.transfer(y - init, "1")
            self.transfer(h, "0")
            init = y + h
        print("")
            
    
    def parallel(self) -> None:
        "Executes processing operations in parallel"
        while True:
            try:
                frame = self.q.get(block=False)
            except:
                if self.flag:
                    return
                else:
                    sleep(0.05) # Adjust
                    continue
            frame = cv2.resize(frame, (640, 480)) # Resize
            frame = frame[:, 220:420] # ROI Cropping
            # Convert the image to grayscale
            gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if self.isStriped(gray_image):
                if self.data is None:
                    self.data = gray_image
                else:
                    self.data = cv2.vconcat([self.data, gray_image])
            else:
                if self.data is not None:
                    self.convert()
                    self.data = None
       

def main() -> None:
    "Just read frame and feed to queue"
    object = receiver()
    cap = cv2.VideoCapture("test1.mp4") # Live video feed here
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
    print("Waiting for daemon thread to join, Closing...")
    thread1.join()

if __name__ == "__main__":
    main()
