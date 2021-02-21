#!/usr/bin/env python
# coding: utf-8

# In[5]:


from shutil import copyfile
import os


# In[3]:


start_fam = '200'
end_fam = '380'


# In[2]:


orig_path = 'resized_fish_pics/'
new_path = 'select_fish_pics/'


# In[7]:


for file in os.listdir(orig_path): 
    if file >= start_fam and file <= end_fam: 
        copyfile(orig_path + file, new_path + file)

