#%%
import torch
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import cv2
# %%
print(f"PyTorch Version: {torch.__version__}")
print(f"Is CUDA available: {torch.cuda.is_available()}")
print(f"opencv version: {cv2.__version__}")
print(f"numpy version: {np.__version__}")
print(f"matplotlib version: {matplotlib.__version__}")
# %%
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True,  device='cpu')

#model = torch.load('yolov5s.pt', map_location=torch.device('cpu'))
# %%



model 

# %%
%matplotlib inline 
img = "cars.jpg"




# %%
results = model(img)
results.print()
# %%
%matplotlib inline 
plt.imshow(np.squeeze(results.render()))
plt.show()
# %%
results.render()
# %%

videos = 'video/cars.mp4'
cap = cv2.VideoCapture(3)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# %%
