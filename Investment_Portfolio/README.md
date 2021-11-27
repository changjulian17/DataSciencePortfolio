
# NARRATIVE
> audience: Investors

Background: Traditional moving away from [60/40](https://www.gsam.com/content/gsam/us/en/individual/market-insights/gsam-connect/2021/is-the-60-40-dead.html). Although there are more assets than equities and fixed income. The [dragon portfolio](https://www.artemiscm.com/artemis-dragon) strategy proposes a multi-generational investment that utilises investment into diversified assets. This portfolio uses majority of trading assets available i.e. equities, fixed income, commodities, gold, long volatility. Therefore it provides a balanced approach to diversify risk.

Taking the dragon portfolios idea of diversification one step further I implemented the use of [Modern Portfolio Theory](https://medium.com/@changjulian17/modern-portfolio-theory-with-python-f33c9f517cd4) to allocate a multi-asset portfolio. It even allows for an investor to adjust their portfolio based on risk. However MPT is an aggregated metric, uses a fixed timeframe and assumes returns have a normal distribution. Ironically that layers more risk. There is still room to improve think multi-asset trading.

This led me to think: "I can't memorise, synthesize and weigh all asset performance to allocations, but a algo probably can".  Combining my interest in portfolio management and data, this project would access the performance of Deep Reinforcement Learner in an investment environment.

# PROBLEM STATEMENT
Create a Reinforcement Learning agent to daily allocate a multi-asset portfolio. Then compare the performance against a random agent and Dragon Portfolio.

# INPUTS
A. list of historical indices / stocks.  
B. Dragon portfolio weights  

## LIBRARIES
1. FinrRL   
	- [**FinRL**](https://finrl.readthedocs.io/en/latest/index.html) is the first open-source framework to demonstrate the great potential of applying deep reinforcement learning in quantitative finance. We help practitioners establish the development pipeline of trading strategies using deep reinforcement learning (DRL).

2. Stable-baselines3
	- [Stable Baselines3 (SB3)](https://github.com/DLR-RM/stable-baselines3)  is a set of reliable implementations of reinforcement learning algorithms in PyTorch. It is the next major version of  [Stable Baselines](https://github.com/hill-a/stable-baselines).

## CONSTRAINTS
A. dividends not includes
B. 5 main asset classes used 
- Equity
	- '^SP500TR' 
		- total return includes dividend from 1988 onwards
	- 'EEM' 
- Fixed Income 
	- 'IEF' 
		- T-bill returns from 2002 onwards
	- 'AGG' 
		- Corporate bond index
- Commodities 
	- '^BCOM' 
		- Commodity index from 2006 onwards
- Gold
	- London gold index 'LBMA Gold Price' [excel](https://www.gold.org/goldhub/data/gold-prices) from 1988 onwards -  
- Long-volatility (eurohedge log vol)    
	- 'Euro hedge long-vol' [excel](https://www.eurekahedge.com/Indices/IndexView/Eurekahedge/640/CBOE-Eurekahedge-Long-Volatility-Hedge-Fund-Index) from 2005 onwards

C. Deep Reinforcement PPO 

### Date Range
Prices will be used from 2005 onwards due to the late adoption of long-vol strategy. 
> Date Range 2004-12-01 to 2021-9-01


# DEVELOPMENT STAGES
1. Make platform for portfolio construction 
    a. get the data with API (DONE)
    b. create low-risk and optimal portfolio (DONE)
2. Predictions
    b. Feature engineering (Calculate MACD and RSI as an extra features)
	    i. use FinRL API to consolidate stocks and features
	c.  Create models to reallocate portfolio daily based on closing prices
	i. MPT
	ii. RL PPO model
	d. compare MPT and RL
3. dashboard with inputs from above

## Challenges
1. **Stationarity**
	- As with most modelled time-series problems stationarity is important when the model is not catered for it. States given to the agent are as stationary as possible and the agent is not given any time dimensions. Instead it is provided:
		- covariance matrix
		- MACD 30-day index
		- RSI 30-day index
		- 1-day close price delta
		- 30-day close price delta
		- 60-day close price delta
2. **Reward**
	- Though both supervised and reinforcement learning use mapping between input and output, unlike supervised learning where feedback provided to the agent is correct set of actions for performing a task, reinforcement learning uses rewards and punishment as signals for positive and negative behavior.
![KD_nuggets_RLagent_flowchart](https://www.kdnuggets.com/images/reinforcement-learning-fig1-700.jpg)
	-  The objective of agent is to get high returns. Where one option is to use daily return as the reward, it may be 'reward rich'. For this project the reward is set to the net of the daily return of the agent and the dragon portfolio.
3. **Exploration vs Exploitation**
	- [Discovery](https://towardsdatascience.com/intuition-exploration-vs-exploitation-c645a1d37c7a) is very important for DRL agents because it does not have any context when acting on the environment. The model did not explore the current solution until the entropy coefficient was .01 (high) and total_timesteps hit 5,120,000 (3 hours running).
5. **Overfitting**
	- PPO and stochastic policy gradient descent problems are notorious for overfitting. This is the case here for PPO. This may be because of the size of the learning rate and clipping resulting in reduced steps in the gradient. This may result in overfitting of trained states but under fitting other dimensions. Example, a solution for a trade within a day in the training set may be relevant for a month of return in the test set. A possible [solution](https://arxiv.org/abs/1907.06704) proposed is to run the training for longer.

#  Files
├── README.md
├── data
│ ├── gold.xlsx
│ ├── long-vol.xlsx
│ ├── processed_data.pkl
│ ├── processed_data_1.pkl
│ └── processed_data_2.pkl
├── modern_portfolio_theory
│ ├── data
│ │ ├── gold.xlsx
│ │ └── long-vol.xlsx
│ └── ticker_data.ipynb
├── preprocessing.ipynb
└── train.ipynb



> Written with [StackEdit](https://stackedit.io/).

