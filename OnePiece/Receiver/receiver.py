# Cetrion 2023
# This program should be able to decode arbitrary number of similar bit sequence.
# for that thickness of the strips must be very large compared to shutter loss
# Todo: Check for possible memory overflow for queue operation
import cv2
from queue import Queue
from time import sleep
import numpy as np
import warnings

class receiver:
    def __init__(self, callback) -> None:
        self.callback = callback
        self.stream = ""
        self.q = Queue()
        self.flag = False
        self.counter = 0
        self.width_dark = 7
        self.width_bright = 13
        self.frame_width = 640
        self.frame_height = 480
        self.length = 19
    

    def isStriped(self, gray_image, brightness_threshold = 150) -> bool:
        "Check if a frame is striped"
        # Apply Canny edge detection
        edges = cv2.Canny(gray_image, threshold1=100, threshold2=200) # Calibrate here
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            average_bright = gray_image[edges > 0].mean()
            
        if np.isnan(average_bright):
                return False
        if average_bright < brightness_threshold:
            return True
        return False
    

    def transfer(self, h, type, width) -> None:
        "Converts height to number of bits"
        # Reduce the effective shutter loss value
        no = round(h / width)
        no = 2 if no > 2 else no
        #print(f'[{no}, {type}]', end = " ")
        self.stream += type*no
        self.counter += no
        

    def convert(self, gray_image) -> None:
        "Retrieves Binary data from B&W image"
        # Apply binary threshold to segment black strips
        _, binary_image = cv2.threshold(gray_image, 50, 250, cv2.THRESH_BINARY_INV) # Calibrate here
        # Find contours in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        init = None
        for contour in reversed(contours):
            x, y, w, h = cv2.boundingRect(contour)
            #print(f'[{y}, {h}]', end = " ")
            if init:
                white_width = y - init
                if white_width > 30:
                    self.stream = ""
                    self.counter = 0
                else:
                    self.transfer(white_width, "1", self.width_bright)
            init = y + h
            if y: # In case we get half of black strip at the start of the frame
                self.transfer(h, "0", self.width_dark)
            if self.counter == self.length:
                self.callback(self.stream)
        self.stream = ""
        self.counter = 0
    
    
    def parallel(self) -> None:
        "Executes processing operations in parallel"
        ROI_left = self.frame_width // 2 - 25
        ROI_right = self.frame_width // 2 + 25
        while True:
            try:
                frame = self.q.get(block=False)
            except:
                if self.flag:
                    return
                else:
                    sleep(0.05) # Adjust
                    continue
            frame = cv2.resize(frame, (self.frame_width, self.frame_height)) # Resize
            frame = frame[:, ROI_left : ROI_right] # ROI Cropping
            # Convert the image to grayscale
            gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if self.isStriped(gray_image):
                cv2.imwrite("Frame.jpg", gray_image)
                self.convert(gray_image) # Appends binary data to self.stream
                #print(self.q.qsize())
                #self.callback(self.stream) # Decode The Stream
       
