import pandas_datareader.data as pdr #Added to bring in Yahoo Finance Data
import datetime as dt #Added to bring in Yahoo Finance Data

def yahooData(ticker):
    start = dt.datetime(2016, 3, 31)
    end = dt.datetime(2021, 11, 17)
    dataset = pdr.get_data_yahoo(ticker, start=start, end=end, interval='d')
    dataset_filtered = dataset[["High", "Low", "Open", "Close"]]
    return dataset_filtered