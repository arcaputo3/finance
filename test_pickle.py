# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:11:18 2018

@author: caputr
"""

import pickle

with open('ticker_data.pkl','rb') as f:
    stock_data = pickle.load(f)
    
