# COVID19-StockMarket Project: "COVID-19 and its Impact on Different Sectors of the Economy Utilizing Stock Market Data"
DS340W Project. Writing a paper to link COVID-19 events with changes in the stock market. Goal is to compare 5 different indexes based on 5 different industries. Then, based on accuracy of predictions, we'd then be able to quantify the impact of COVID-19 on different areas of the market. We looked at the following indexes:
- XLE: Energy Select Sector SPDR Fund
- XLF: Financial Select Sector SPDR Fund
- XLI: Industrial Select Sector SPDR Fund
- XLK: Technology Select Sector SPDR Fund
- XLV: Health Care Select Sector SPDR Fund


Link to Parent Paper: https://journalofbigdata.springeropen.com/articles/10.1186/s40537-021-00430-0

Link to our Paper: https://docs.google.com/document/d/18d7qYq9roBATgZy4zkRg8aqqN_gCHLqL/edit?usp=sharing&ouid=109867115804583300351&rtpof=true&sd=true

## ***_Implementation.ipynb
These Jupyter notebooks house results for each stock index. A clear data pipeline can be traced for each.

## preprocessing.py
This Python script is brought in in order to convert 1D data into a time series before predictions are made. This script was created by the authors of our paper

## yahoodata.py
This Python script is brought in in order to bring in data for a given ticker. The function within this script takes in 7 parameters, where one is for the ticker and the other 6 define the dates pull from Yahoo Finance. This was created originally by our group.

## images folder
This folder contains images of all the results (including the lag Jupyter Notebook) after models are created for each index.

## XLV_Implementation_Lag.ipynb
After identifying the present of data lag, this notebook was used to explore a shorter time frame of data. This way, we can drill down to visually see the lag happening. This was done with the stock index for the Health Care Select Sector SPDR Fund, ticker XLV.
