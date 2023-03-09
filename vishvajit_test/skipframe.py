import cv2 

vidcap =cv2.VideoCapture(0)
fps = vidcap.get(cv2.CAP_PROP_FPS)
print(f"row fps: {fps}")

count = 0

skip = 10

success = True

while success:
    success,image = vidcap.read()
    if count % skip == 0:
        cv2.imshow('came', image)    # save frame as JPEG file      
    count += 1
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    print(f"row fps: {fps}")
    
    
    c = cv2.waitKey(1)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

vidcap.release()
cv2.destroyAllWindows()
