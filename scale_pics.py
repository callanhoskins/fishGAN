#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import cv2


# In[22]:


files_paths = os.listdir("fish_pics/")


# In[27]:


def crop_img(img): 
    center = (img.shape[0]//2, img.shape[1]//2)
    half_len = min(center[0], center[1])
    img = img[center[0]-half_len:center[0]+half_len, center[1]-half_len:center[1]+half_len]
    return img


# In[28]:


for file in files_paths: 
    print(file)
    try:
        image = cv2.imread('fish_pics/' + file)
        image = crop_img(image)
        image = cv2.resize(image, (256, 256))
        cv2.imwrite('resized_fish_pics/' + file, image)
    except AttributeError as e: 
        print(e)

