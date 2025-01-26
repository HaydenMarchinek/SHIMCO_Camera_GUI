# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:07:49 2025

@author: hayde
"""

import matplotlib.pyplot as plt
import numpy as np
import pylablib as pll
import time
import datetime
import os

EXPOSURETIME = 100 #ms
FILENAMEPREFIX = 'Tempfilename'
NUMEXPOSURES = 3


# Fixing the file path using a raw string
pll.par["devices/dlls/picam"] = "C:\\Program Files\\Princeton Instruments\\PICam\\Runtime\\Picam.dll"

from pylablib.devices import PrincetonInstruments

# List available cameras and initialize one
print(PrincetonInstruments.list_cameras())

# # Initialize the camera with a valid serial number 
cam = PrincetonInstruments.PicamCamera('0809080002')

Images = []
# with PrincetonInstruments.PicamCamera('0809080002') as cam:
cam.set_attribute_value('Exposure Time', EXPOSURETIME)
cam.start_acquisition()
while True:
    if len(Images) < NUMEXPOSURES:                
        cam.wait_for_frame()
        image = cam.read_oldest_image()
        Images.append(image)
    else:
        break
cam.stop_acquisition()
print(Images)
plt.imshow(image)
plt.show()
# for image in Images:
#     current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     filename = f"{FILENAMEPREFIX}_{current_time}"    
#     file_path = os.path.join("C:\\Users\\hayde\\OneDrive\\Desktop\\images", filename)
#     image.tofile(file_path + '.bin')
