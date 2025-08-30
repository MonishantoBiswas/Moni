class ROI_based_img_crop:
    import cv2

    cap = cv2.VideoCapture(1)
    # ret,frame=cap.read()
    # frame=cv2.resize(frame,(640,480))
    # roi=cv2.selectROI(frame)

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 480))
        roi = frame[100:350, 300:550]
        cv2.imshow("FRAME", frame)
        cv2.imshow("ROI", roi)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


