#!/usr/bin/env python
# coding: utf-8

# In[1]:

import PIL.ImageGrab
import pyautogui
import matplotlib.pyplot as plt
import numpy as np
import time
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'



# In[3]:


centerx = 230
centery = 315
width = 40
im = PIL.ImageGrab.grab()
img = np.array(im)
plt.imshow(img[(centery-width):(centery+width),(centerx-width):(centerx+width)])
plt.show()
print(pytesseract.image_to_string(img[(centery-width):(centery+width),(centerx-width):(centerx+width)], lang='eng'))
