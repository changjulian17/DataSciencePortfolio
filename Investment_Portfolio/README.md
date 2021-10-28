
# NARRATIVE
audience: Investors
moving away from 60/40 to 80/20 portfolio
alternative: dragon portfolio



# SUB-PROJECTS
1. portfolio construction 
	 - [ ]  VaR + allocation
2. prediction
	 - [ ] Predict VaR (options pricing?)
	 - [ ] NLP

# INPUTS
a. list of historical indices / stocks
b. risk level 0-10
c. composition of portfolio (e.g. 60/40, 80/20)

sources: Quandl - Yahoo finance / Alpha Vantage

# CONSTRAINTS
a. do not include dividends
b. ensure 5 sectors 
1. equity (snp500 + world)
2. FI (T-bill+corpbonds index)
3. commodity (commodity index)
4. gold (london gold index)
5. long-vol (eurohedge log vol)    

Actual tickers used: 
1. '^SP500TR' (total return inc. div, oldest up to 1988) + 'IWDA.L' (oldest up to 2009)
2. 'IEF' (oldest up to 2002) + 'LQD' (up to 2002 !dividend distributed)
3. 'DJP' (up to 2006)
4. 'LBMA Gold Price' excel (1988) -  https://www.gold.org/goldhub/data/gold-prices
5. 'Euro hedge long-vol' excel (2005) - https://www.eurekahedge.com/Indices/IndexView/Eurekahedge/640/CBOE-Eurekahedge-Long-Volatility-Hedge-Fund-Index

### Date Range  
2004-12-01  
2021-09-31

c. 2005 onwards (due to long-vol limitations)


# DEVELOPMENT STAGES
1. Make platform for portolio construction
    a. get the data with API
    b. create low-risk and optimal portfolio
2. Predictions
    a. calculate future returns with Vector Auto-regression?
    b. Forward predictions (reinforcement model)
    (optional) Calculate MACD and RSI as an extra features
3. dashboard with inputs from above


> Written with [StackEdit](https://stackedit.io/).

