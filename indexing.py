#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:01:33 2018
#Indexing image dataset
@author: manisha
"""

from RGBHist import RGB
import argParse
import cPickle
import glob
import cv2

#Parsing arguments for dataset and index
ap = argParse.ArgumentParser()
ap.addArgument("--d", "--dataset", required=True, help="Path to dictionary that contains the images to be indexed")
ap.addArgument("--i","--index", required=True, help="Path to where computed index will be stored")
args = vars(ap.parse_args())
#initializing index dictionary to store the filename(key) and histogram(value) for each image
index={}
#instantiate RGB with 8 bins per color
desc = RGB([8,8,8])
for imagepath in glob.glob(args["dataset"] + "/*.png"):
    #extract file name --> key
    k = imagepath[imagepath.rfind("/")+1:]
    #Load image and describe using RGB hist descriptor
    image = cv2.imread(imagepath)
    feature = desc.decribe(image)
    index[k] = feature
    
#Now indexing our image..
f = open(args["index"], "w")
f.write(cPickle.dumps(index))
f.close()
 
