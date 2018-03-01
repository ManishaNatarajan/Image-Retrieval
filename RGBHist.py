#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:48:28 2018
To design a Content Based Image Retreival System
@author: manisha
"""
#importing packages
import cv2
import numpy as np

#Defining image descriptor based on RGB color Histogram
class RGB:
    def __init__(self, bins):
        #Storing bins for histogram
        #Computing 3D histogram with 8 bins
        self.bins = bins
        
    def describe(self, image):
        #Create a 3D histogram in RGB colorspace and normalize it
        hist = cv2.calcHist([image], [0, 1, 2], None, self.bins, [0, 256, 0, 256, 0, 256])
        hist_norm = cv2.normalize(hist)
        return hist_norm.flatten()
        
