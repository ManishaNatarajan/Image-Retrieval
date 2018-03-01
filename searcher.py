#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:42:09 2018
Class for Image Search
@author: manisha
"""
import nupy as np
class Search:
    def __init__(self, index):
        #store inddex of images
        self.index = index
    
    def search(self, queryFeature):
        results = {}
        for (k,features) in self.index.items():
            d = self.chi2distance(features,queryFeature)
            results[k] = d
            
        results = sorted([(v, k) for (k,v) in results.items()])
        
        return results
    
    def chi2distance(self, histA, histB, eps = 1e-10):
        #Compute chi_squared distance between feature vectors of images
        d = 0.5*np.sum([((a-b)**2)/(a+b+eps) for (a,b) in zip(histA, histB)])
        #Return the computed distance
        return d
    
    
