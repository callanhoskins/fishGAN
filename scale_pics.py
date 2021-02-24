#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import cv2


# In[22]:


files_paths = os.listdir("fish_pics/")

MAX_FAM = '370'
MIN_FAM = '349'


# In[27]:

# This function crops the image to be square with its dimensions min(height, width) x min(height, width)
def crop_img(img): 
    center = (img.shape[0]//2, img.shape[1]//2)
    half_len = min(center[0], center[1])
    img = img[center[0]-half_len:center[0]+half_len, center[1]-half_len:center[1]+half_len]
    return img

# This function zero-pads the image on the top so that it's a square
# can change the code to zero-pad it on the side
def zero_pad_img(img):
    height, width, channels = img.shape
    pad_amt = (width - height) // 2
    img = cv2.copyMakeBorder(img, pad_amt, pad_amt, 0, 0, cv2.BORDER_CONSTANT, value=0)
    return img


# In[28]:

if __name__ == '__main__':
    for file in files_paths:
        if file <= MAX_FAM and file >= MIN_FAM:
            image = cv2.imread('fish_pics/' + file)
            image = zero_pad_img(image)
            image = cv2.resize(image, (256, 256))
            cv2.imwrite('resized_fish_pics/' + file, image)

