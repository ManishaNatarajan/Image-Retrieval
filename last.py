#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:00:38 2018

@author: manisha
"""

from searcher import Search
import numpy as np
import argParse
import cPickle
import cv2

ap = argParse.ArgumentParser()
ap.add_argument("--d","--dataset", required = True, help = "Path to the directory that contains images that indexed")
ap.add_argument("--i", "--index", required = True, help = "Path to where we stored our index")
args = vars(ap.parse_args())

#Load the index and initialize searcher
index = cPickle.loads(open(args["index"]).read())
searcher = Search(index)



