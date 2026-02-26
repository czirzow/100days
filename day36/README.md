
### setting up environment:
Ensure you are in venv:
  >source .venv/bin/active

Setup Vantage key:
  >export VANTAGE_API_KEY=YOURKEY




## Stocks News Monitoring Project
Get a stock symbol check it's status and if certain conditions exits
send an email of news about that stock symbol.


### agenda
- get stock market data:
  - when market closed value
  - when market closed the previous day
    - check the difference in value
    - and calculate percentage.
  - if percentage > 10%, or some percentage
    - retrieve news data related to symbol
- with the news send an email.

### Plan of Attack
- start base main.py
  - refacter the Mail() lib i created earlier
  - refacter the Cache() config.
  - create a basic API class that  marketdata and newsdata inherits
    - Create the classes to handle marketdata and newsdata
  - include them into the project.


## references
- [stock market Data Api](https://www.alphavantage.co/)
- [news api](https://www.alphavantage.co/)
- [NASDAQ-TSLA](https://www.tradingview.com/symbols/NASDAQ-TSLA/)



