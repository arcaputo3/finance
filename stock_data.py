'''
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
# Alpha Vantage Key: MTGXUV03HPBVT0TO
key = 'MTGXUV03HPBVT0TO'

ts = TimeSeries(key=key, output_format='pandas',indexing_type='date')
data1, meta_data = ts.get_intraday(symbol='MSFT', interval='1day', outputsize='full')


'''
from datetime import datetime
import fix_yahoo_finance as yf
import pandas as pd
import pickle

companies = pd.read_csv('companylist.csv')

tickers = list(companies[companies['MarketCap'] >= companies['MarketCap'].quantile(0.95)]['Symbol'].values)

top_ticker_data = {}

for ticker in tickers:
    top_ticker_data[ticker] = yf.download(ticker,'2000-01-01', str(str(datetime.now())[:10]))

with open('ticker_data.pkl', 'wb') as f:
    pickle.dump(top_ticker_data, f)
