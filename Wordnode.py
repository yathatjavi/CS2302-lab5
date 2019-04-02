# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:01:53 2019

@author: yatha
"""
import numpy as np

class Word(object):
    
    def __init__(self,wordAndEm=None):
        #will take a list use the forst item in the list as the text and the
        #remaining 50 items as the embedding 
        #creates a node (Word) to be used in hastables and bst
        items = wordAndEm.split()
        self.text = items.pop(0)
        self.embedding = np.array(items, dtype=np.float)
        
def printWord(W):
    print(W.text)

