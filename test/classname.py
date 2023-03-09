#%%
import numpy as np
from torch import le 
from config import cfg


#%%
def read_class_names(class_file_name):
    names = {}
    with open(class_file_name, 'r') as data:
        for ID, name in enumerate(data):
            names[ID] = name.strip('\n')
    return names
# %%

NUM_CLASS = len(read_class_names(cfg.YOLO.CLASSES))
# %%
class_names = read_class_names(cfg.YOLO.CLASSES)
# %%
classes = list(class_names.values())
# %%

allowed_classes = ['person', 'car', 'truck', 'bus', 'motorbike', 'bicycle'] 

# %%

# %%

# %%

cls_idx = []

for allowed_class in allowed_classes:
    #print(i, allowed_classes[i])
    a = classes.index(allowed_class)
    print(a)
    cls_idx.append(a)


print(cls_idx) 
# %%
import pandas as pd


datafram = pd.read_csv("BRC_val.csv")
# %%
datafram.head()
# %%

datafram.columns
# %%
datafram['xmin']
# %%

datafram['xmin'].valu_counts()
# %%
datafram.describe()
# %%
