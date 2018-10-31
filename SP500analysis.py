# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 16:48:45 2018

@author: caputr
"""

import pandas as pd
from datetime import datetime
import fix_yahoo_finance as yf
import pickle

data = pd.read_csv('all_stocks_5yr.csv')
close = data[['date','close','Name']]
close = close.pivot(index='date',columns='Name',values='close')

tickers = list(close.columns)

top_ticker_data = {}

for ticker in tickers:
    try:
        top_ticker_data[ticker] = yf.download(ticker,'2010-01-01', str(str(datetime.now())[:10]))['Adj Close']
    except Exception:
        pass

top_ticker_data = pd.DataFrame(top_ticker_data)

with open('ticker_data.pkl', 'wb') as f:
    pickle.dump(top_ticker_data, f)

