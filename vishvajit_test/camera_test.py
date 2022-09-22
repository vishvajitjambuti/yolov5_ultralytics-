import cv2

cap = cv2.VideoCapture(3)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.9, fy=0.9, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)
    
    #fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(fps)
    #print(f"Frames per second using {fps}")


    c = cv2.waitKey(1)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()