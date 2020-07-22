#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PIL.ImageGrab
import pyautogui
import matplotlib.pyplot as plt
import numpy as np
import time


# In[100]:


points = {"Wizard":(800,680),
            "Heli" : (580,520),
            "Home" : (830,820),
            "Restart1" : (1085,810),
            "Restart2" : (1130,720),
            "ClearMonkey" : (1750,820),
         }
keys = {"Wizard":'a',
         "Heli" : 'b',
        "Upgrade1" : ",",
        "Upgrade2" : ".",
        "Upgrade3" : "/",
        "Clear" : "Esc",
         }


# In[99]:


def getSnap(debug=False):
    im = PIL.ImageGrab.grab()
    if (debug):
        img = np.array(im)
        plt.imshow(img)
        plt.show()
    print(img.shape)
    return np.array(im)

def getSquare(point,width = 100,height=100,debug=False):
    centerX,centerY = point
    im = PIL.ImageGrab.grab()
    img = np.array(im)
    img = img[(centerY-height):(centerY+height),(centerX-width):(centerX+width)]
    if (debug):
        plt.imshow(img)
        plt.show()
    return img

getSnap(True)
# getSquare((165,380),debug=True).shape
getSquare((580,520),debug=True).shape


# In[105]:


def placeMonkey(name,debug=False):
    if (debug):
        i = 3
        while (i > 0):
            time.sleep(1)
            print("Placing in " + str(i),end='\r')
            i -= 1
        print("\nDropping")
    pyautogui.moveTo(points[name])
    pyautogui.keyDown(keys[name])
    pyautogui.keyUp(keys[name])
    pyautogui.click(points[name])
    pyautogui.moveTo(points["ClearMonkey"])
    
def upgradeMonkey(name,upgrade,debug=False):
    if (debug):
        i = 3
        while (i > 0):
            time.sleep(1)
            print("Upgrading in " + str(i),end='\r')
            i -= 1
        print("\nUpgrading")
    pyautogui.moveTo(points[name])
    pyautogui.click(points[name])
    pyautogui.keyDown(keys[upgrade])
    pyautogui.keyUp(keys[upgrade])

# placeMonkey("Wizard",True)
placeMonkey("Heli",True)
upgradeMonkey("Heli","Upgrade2")


# In[ ]:




