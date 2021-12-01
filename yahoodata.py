import pandas_datareader.data as pdr #Added to bring in Yahoo Finance Data
import datetime as dt #Added to bring in Yahoo Finance Data

def pullStockData(ticker, start_year, start_month, start_day, end_year, end_month, end_day):
    """
    ticker = string: ticker of desired stock
    start_year = int: starting year for range
    start_month = int: starting month for range
    start_day = int: starting day for range
    end_year = int: ending year for range
    end_month = int: ending month for range
    end_day = int: ending day for range
    """
    start = dt.datetime(start_year, start_month, start_day)
    end = dt.datetime(end_year, end_month, end_day)
    dataset = pdr.get_data_yahoo(ticker, start=start, end=end, interval='d')
    dataset_filtered = dataset[["High", "Low", "Open", "Close"]]
    return dataset_filtered