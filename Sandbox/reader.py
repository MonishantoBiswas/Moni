## Saikat Chakraborty
import cv2
import numpy as np

single, double = [26, 28], [56, 58] # lower and upper limit of strip heights
# 32,  62 for bright strips, calibration may be required
shutter_loss = 7 # Pixel loss due to frame transitioning
prev_strip = None
bit_seq = []

def calculate_strip_properties(gray_image):
    
    # Apply binary threshold to segment black strips
    _, binary_image = cv2.threshold(gray_image, 80, 200, cv2.THRESH_BINARY_INV) # Calibrate here
    # The value of the 2nd argument is the lower limit of brightness,
    # which is the average value of dark pixels (average_dark)
    # Similarly 3rd arg is average_bright
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    global prev_strip
    
    initial_height = None
    
    for contour in reversed(contours):
        x, y, w, h = cv2.boundingRect(contour)
        # Check for bright strips
        if initial_height:
            diff = y - initial_height
            if diff >= single[0] and diff <= single[1]:
                bit_seq.append(1)
            elif diff >= double[0] and diff <= double[1]:
                bit_seq += [1, 1]
        else:
            initial_height = 0
        # Check for dark strips
        if prev_strip:
            h += prev_strip + shutter_loss
            prev_strip = None
        if h >= single[0] and h <= single[1]:
            bit_seq.append(0)
        elif h >= double[0] and h <= double[1]:
            bit_seq += [0, 0]
        initial_height += y + h
        if initial_height == 480: # window height
            prev_strip = h

def isStriped(image, brightness_threshold=100) -> bool:

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, threshold1=100, threshold2=200) # Calibrate here
    # For instance, you can calculate the average pixel intensity of bright and dark areas
    average_bright = gray_image[edges > 0].mean()
    print(average_bright)

    ## Condition to declare: May be changed
    if average_bright > brightness_threshold:
        return False
    calculate_strip_properties(gray_image)
    return True



def main():
    cap = cv2.VideoCapture("test.mp4")
    # ret, frame = cap.read()
    # gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # calculate_strip_properties(gray_image)
    counter = 0
    #length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    while cap.isOpened():
        ret, frame = cap.read()
        counter += 1
        
        if ret == True:
            frame = cv2.resize(frame, (640, 480))
            # ROI Cropping
            frame = frame[:, 220:420]
            #print(counter, end=" ")
            #print(f"/rFrames:{counter}/{length}", end="")
            #cv2.imshow('frame', frame)
            if isStriped(frame):
                pass
                #print(counter)
                #cv2.imshow(str(counter), frame)
            if cv2.waitKey(27) & 0xFF == ord('q'):
                break
        else:
            break
    print(bit_seq)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        return

if __name__ == "__main__":
    main()