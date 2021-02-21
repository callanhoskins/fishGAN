#!/usr/bin/env python
# coding: utf-8

# In[6]:


import selenium
import requests
from bs4 import BeautifulSoup


# In[11]:


url_index = 'https://www.fishbase.us/photos/FamilyThumbnailsSummary.php?famcode='
url_photo = 'http://d1iraxgbwuhpbw.cloudfront.net/images/species/'
fam_code = '10'
species_name = 'ceven_u1.jpg'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
MAX_PAGE = 595


# In[24]:


def get_image_names(url): 
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    images = soup.find_all('img')
    img_names = [img['src'].lower() for img in images]
    return [name[name.find('_')+1:] for name in img_names]


# In[25]:


def download_image(species_name, fam_code): 
    r = requests.get(url_photo + species_name, headers=headers)
    with open('fish_pics/' + fam_code.zfill(3) + '_' + species_name, 'wb') as f: 
        f.write(r.content)


# In[26]:


for fam_code in range(407, MAX_PAGE): 
    fam_code = str(fam_code)
    print('{}: '.format(fam_code), end='')
    img_names = get_image_names(url_index + fam_code)
    for name in img_names:
        download_image(name, fam_code)
        print('*', end='')
    print()

