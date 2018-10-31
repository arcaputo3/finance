# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:11:18 2018

@author: caputr
"""

import pickle
import pandas as pd

with open('ticker_data.pkl','rb') as f:
    stock_data = pickle.load(f)

stock_data.dropna(axis=1, inplace=True)
print(stock_data.keys())

writer = pd.ExcelWriter('SP500closes.xlsx')
stock_data.to_excel(writer,'Close')
writer.save()