from threading import Thread
from queue import Queue
import cv2
import time

q = Queue(maxsize=10)

def process() -> None:
    "Process a frame and show result"
    while True:
        try:
            image = q.get(block=False)
        except q.empty:
            return
        # Process Image
        pass

def main() -> None:
    "Main function of the program"
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        try:
            q.put(frame, block=False)
        except q.full:
            thread = Thread(target=process, daemon=True)
            thread.start()
            q.put()