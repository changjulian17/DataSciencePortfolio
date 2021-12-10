
# AI Portfolio Allocator
> Medium articles:  
[<img alt="medium articles" width="22px" src="https://raw.githubusercontent.com/iconic/open-iconic/master/svg/globe.svg" /> Assumptions](https://medium.com/@changjulian17/reinforcement-learning-ppo-in-an-investment-environment-c18b1bac29c4)  [<img alt="medium articles" width="22px" src="https://raw.githubusercontent.com/iconic/open-iconic/master/svg/globe.svg" /> Model Parameters](https://medium.com/@changjulian17/portfolio-allocation-reinforcement-learning-ppo-model-part-i-5cabd5aaaa93)  
[<img align="left" alt="website" width="22px" src="https://raw.githubusercontent.com/iconic/open-iconic/master/svg/laptop.svg" />   AI Portfolio Allocator website ](https://ai-portfolio-allocator.herokuapp.com)  
[<img align="left" alt="medium articles" width="22px" src="https://raw.githubusercontent.com/iconic/open-iconic/master/svg/clipboard.svg" /> Tensorboard](https://tensorboard.dev/experiment/z20zIbr6TmSQ3vqUBTpkAw/#scalars)  
[<img align="left" alt="medium articles" width="22px" src="https://raw.githubusercontent.com/iconic/open-iconic/master/svg/script.svg" />  Repository](https://github.com/changjulian17/DataSciencePortfolio/tree/main/Investment_Portfolio)  

## Background 

Traditional investors are starting moving away from [60/40](https://www.gsam.com/content/gsam/us/en/individual/market-insights/gsam-connect/2021/is-the-60-40-dead.html) equities/fixed income strategies to provide a long term return. Although there are more assets than equities and fixed income. The trademarked [Dragon portfolio](https://www.artemiscm.com/artemis-dragon) strategy proposes a multi-generational investment that utilises investment into diversified assets. This portfolio integrates popularly traded asset classes i.e. equities, fixed income, commodities, gold, long volatility. The main objective of the portfolio is to provide stable wealth accumulation for 100 years.

To understand the Dragon portfolio better I implemented the use of [Modern Portfolio Theory](https://medium.com/@changjulian17/modern-portfolio-theory-with-python-f33c9f517cd4) with python code to allocate a multi-asset portfolio. It even allows for an investor to adjust their portfolio based on risk. However MPT is an aggregated metric, using a fixed timeframe and assumes returns have a normal distribution. Ironically that layers more risk. There is still room to improve multi-asset trading.

This led me to think: “I can’t memorise, synthesise and weigh all asset performance to allocations, but a model would”. So my goal is to learn Reinforcement Learning (RL) by building a RL model that will trade and  at the same time determine if it can beat a benchmark.

## Problem Statement
**This project assessed the performance of Deep Reinforcement Learning (RL) in an investment environment. Model performance was compared against the Dragon portfolio** in a backtest from 2020 to 2021.

## About the Project
### Proposal
In addition to the below, prepared  proposal [here](https://docs.google.com/document/d/1JTtCsagoKAtkpOO9RwbSwYwk30QeEvKvym455RIAzrU/edit?usp=sharing)
### Inputs
A. List of historical indices / stocks.  
B. Dragon portfolio weights  

### Constraints
A. Dividends not included.  
B. Transaction fees are not accounted for in the reward or returns computation  
C. 5 main asset classes used   
D. Deep Reinforcement Learning model using PPO  
	- PPO is a on-policy gradient descent algorithm  
E. Date Range   
	- Prices will be used from 2005 onwards due to the late adoption of long-vol strategy.  
	- Date Range 2004-12-01 to 2021-9-01  

## Development Stages
1. Make platform for portfolio construction 
    a.  Compile historical stock data  
2. Feature engineering - Enrich stock prices- See notebook [`preprocessing.ipynb`](https://github.com/changjulian17/DataSciencePortfolio/blob/main/Investment_Portfolio/preprocessing.ipynb)  
	a. Moving Average Convergence Divergence [(MACD)](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiU_uHLxbz0AhUSheYKHUb7Dd8QtwJ6BAgNEAM&url=https%3A%2F%2Fwww.investopedia.com%2Fterms%2Fm%2Fmacd.asp&usg=AOvVaw2xh3SBw1WyNdcJ_481DNVi).  
	b. Relative Strength Index [(RSI)](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiB1KX7xbz0AhXQ8HMBHb9QBRYQtwJ6BAgMEAM&url=https%3A%2F%2Fwww.investopedia.com%2Fterms%2Fr%2Frsi.asp&usg=AOvVaw03QeCun2Y2fpO4fA_ZaFMm)   
	c. Commodity Channel Index [(CCI)](https://www.investopedia.com/terms/c/commoditychannelindex.asp)  
	d. Directional Movement Index [(DMI)](https://www.investopedia.com/terms/d/dmi.asp)    
	e. 30 and 60 day Simple Moving Average [(SMA)](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiGyrekxrz0AhUzILcAHcssDlIQFnoECAQQAQ&url=https%3A%2F%2Fwww.investopedia.com%2Fterms%2Fs%2Fsma.asp&usg=AOvVaw31NjSKUZgU0OJnxkj6nMf3)  
	f. [Covariance Matrix](https://www.investopedia.com/articles/financial-theory/11/calculating-covariance.asp) stock indicators  
	g. Price Close, 30 Day SMA, 60 Day SMA deltas. Is the change in closing price, 30 Day SMA and 60 Day SMA from the previous day  
3. Train Model - See notebook [`train.ipynb`](https://github.com/changjulian17/DataSciencePortfolio/blob/main/Investment_Portfolio/train.ipynb)   
	a. Hyperparameter tuning  
4. Backtest Model  - See notebook [`eval.ipynb`](https://github.com/changjulian17/DataSciencePortfolio/blob/main/Investment_Portfolio/eval.ipynb)  
	a. Get returns for Dragon Portfolio, Minimum Variance and Random Agent Portfolios  
	b. Backtest all portfolios and compare performance
5. Create webapp on Heroku - See [website](http://ai-portfolio-allocator.herokuapp.com)  

## Challenges
1. **Stationarity**  
	- As with most modelled time-series problems stationarity is important when the model is not designed to perform time-series regressions. Choosing stationary indicators and relative price representation is necessary.  
2. **Reward**  
	- n supervised learning instructional feedback is provided to the agent, but reinforcement learning uses reward and punishment as signals for positive and negative behaviour (as a series of actions).  
![KD_nuggets_RLagent_flowchart](https://www.kdnuggets.com/images/reinforcement-learning-fig1-700.jpg)   
	-  For this project the reward is set to the net of the daily return of the agent and the dragon portfolio.  
	- _For this project transaction fees are not taken into account for the reward or the computation of total returns_  
3. **Exploration vs Exploitation**  
	- [Exploration](https://towardsdatascience.com/intuition-exploration-vs-exploitation-c645a1d37c7a) 1.  is very important for DRL agents because it does not have any context when acting on the environment. The model did not explore the current solution until the entropy coefficient was .01 (high) and total_timesteps was 10,240,000 (7 hours running). [Tensorboard](https://tensorboard.dev/experiment/z20zIbr6TmSQ3vqUBTpkAw/#scalars) is online here. After sufficient exploration then we can exploit the experience during the prediction phase.  
4. **Overfitting**  
	- PPO and stochastic policy gradient descent problems are notorious for overfitting. This is the case here where the model had exceptional returns in the training period but disproportionately less in the test environment. This may be because of the size of the learning rate and clipping ratio resulting in reduced iterative steps in the gradient. This would result in fitted weights of trained states but under fitting unseen dimensions and states. For example, a solution for a trade within a day in the training set may be relevant for a full month of return in the test set. A possible [solution](https://arxiv.org/abs/1907.06704) proposed is to run the training for longer.  

## Data References
### Data Dictionary
`./data/processed_data.pkl`
|Column|Description |
|--|--|
| date | date of record |
| month | month of record |
| close | day's closing price |
| volume | day's volume trade, Commodities, Cash, Gold, Long Volatility and S&P 500 may be missing this data |
| tic | ticker |
| macd | MACD indicator |
| rsi_30 | 30-Day RSI indicator |
| cci_30 | 30-day CCI indicater |
| dx_30 | 30-Day DX indicator |
| close_30_sma | 30-day closing price SMA |
| close_60_sma | 60-Day closing price SMA |
| cov_list | covariance with other tickers |
| return_list | list of tickers in cov_list |
| close_delta | difference on previous day's closing price |
| close_30_sma | difference on previous day's 30-day closing price SMA |
| close_60_sma | difference on previous day's 60-Day closing price SMA |

###  Files  
.  
├── README.md  
├── data  
│ └── processed_data.pkl  (processed data output from `preprocessing.ipynb`)  
├── eval.ipynb  (evaluation notebook used to measure model performance and print visualisations)  
├── modern_portfolio_theory  
│ ├── data  
│ │ ├── gold.xlsx  (gold data from 'LBMA Gold Price')  
│ │ └── long-vol.xlsx  (gold data from ‘Euro hedge long-vol')  
│ └── ticker_data.ipynb  (notebook used evaluating MPT)  
├── preprocessing.ipynb  (compile and enrich data to `processed_data.pkl` for training)  
├── results  
│ ├── df_actions_14_4.csv  (PPO 4 2020-2021-Aug daily portfolio allocations)  
│ ├── df_actions_14_5.csv  (PPO 5 2020-2021-Aug daily portfolio allocations)  
│ ├── df_daily_return_14_4.csv  (PPO 4 2020-2021-Aug daily portfolio returns)  
│ ├── df_daily_return_14_5.csv  (PPO 5 2020-2021-Aug daily portfolio returns)  
│ ├── df_drg_returns.csv  (dragon portfolio 2020-2021-Aug daily portfolio returns)  
│ ├── df_minv_returns.csv  (minimum variance portfolio 2020-2021-Aug daily portfolio returns)  
│ ├── df_rand_returns.csv  (random agent portfolio 2020-2021-Aug daily portfolio returns)  
│ └── df_strat_stats.csv  (summary investment stats for 2020-2021-Aug daily portfolio returns)  
├── tensorboard_log  
│ └── ppo  
│├── ppo_14_4_tboard  
│ │ └── events.out.tfevents.1637990385.a89177fd15fc.921.1  (PPO 4 training tensorboard)  
│ └── ppo_14_5_tboard  
│       └── events.out.tfevents.1638169318.ac0d747845b7.66.0  (PPO 5 training tensorboard)  
├── train.ipynb  (train data from `processed_data.pkl` and output trained model, returns and actions from trained model)  
├── trained_models  
│ ├── ppo_14_4.pkl  (PPO 4 model)  
│ └── ppo_14_5.pkl  (PPO 5 model)  
└── webapp  (Heroku webapp files)  
├── Procfile  
├── __pycache__  
│ ├── plotter.cpython-39.pyc  
│ └── util.cpython-39.pyc  
├── app.py  
├── plotter.py  
├── requirements.txt  
├── setup.sh  
└── util.py

> References:
> [_Hypertuning Trials_](https://docs.google.com/spreadsheets/d/1toUbJDoz3u-xMWY5XidHJymkxXeWRiPZ0whZxIAiyvo/edit?usp=sharing)

> Written with [StackEdit](https://stackedit.io/).

