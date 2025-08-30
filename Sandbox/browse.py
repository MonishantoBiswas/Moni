import cv2

# Open the video file
video_path = 'hello2.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video file.")
    exit()

current_frame = 0

while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, (640, 480))
    #roi = frame[:, 220:420]

    if not ret:
        print("End of video.")
        break

    cv2.imshow("ROI", frame)

    key = cv2.waitKey(0)
    current_frame += 1
    if key == ord('n'):
        #continue
        current_frame += 1
        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    elif key == ord('0'):
        current_frame -= 1
        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    elif key == ord('s'):
        frame_filename = f'frame_{current_frame}.jpg'
        cv2.imwrite(frame_filename, frame)
        print(f"Saved frame as {frame_filename}")
    elif key == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
