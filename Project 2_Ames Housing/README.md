# Project 2 - Ames Housing Data and Kaggle Challenge
## Executive Summary
We will build a **Linear Regression with Ridge Regularisation** model for `Ames Housing Data` dataset in order to as accurately predict the sales price of any house in the town of Ames. The dataset consists of robust dataset with over **70** columns of different features relating to houses sold from 2006-2010, relationship of some features will be attempted to be understood. We will predict that not all the factors will can be used to estimate the actual price of an Ames House.

## 1. Introduction
### 1.1 Background
There can be no question that access to housing remains unequal. Despite long-standing laws guarding against discrimination, members of disadvantaged groups have a harder time finding a high-quality place to live in a high-opportunity neighborhood. It’s far less obvious, however, whether—or how much—these disparities result from discrimination, because disadvantaged groups often differ systematically in employment, income, assets, and debts. That’s where the Urban Institute’s paired-testing research comes in.  
  
Paired testing, also known as auditing, is an effective and intuitive way to test whether and in what form discrimination exists. In a paired test, two people are assigned fictitious identities and qualifications that are comparable in all key respects. The identities differ only on the characteristic (for example, race or presence of a disability) being tested. Each tester of a pair then makes a similar request (information on available apartments, for example) and documents the interaction. With an appropriate sample of tests and statistical techniques, paired testing can single out discrimination. 

Ames is a town in the 23rd District of the state of Iowa. The 5 largest ethnic groups in Ames, IA are White (Non-Hispanic) (78.7%), Asian (Non-Hispanic) (11.4%), Black or African American (Non-Hispanic) (3.09%), Two+ (Non-Hispanic) (2.64%), and White (Hispanic) (2.6%). 0% of the households in Ames,
([*source*](https://datausa.io/profile/geo/ames-ia/))

To further objectivity is called besides the above pair testing and it is important to value the true price of a house. Therefore to supplement this it is seen that data science is necessary to estimate the true value of a property based on historical records.([*source*](https://www.urban.org/features/exposing-housing-discrimination))

([*further coverage*](https://www.washingtonpost.com/business/2021/03/18/report-housing-discrimination-renter-buyer/))

### 1.2 Problem Statement: 
The objective of the project is to use Ames Housing data to make a linear regression and regularisation model then use predictors to predict any Ames house sale price. This would most likely be to the benefit of all stakeholders within a house transaction (e.g. buyers, sellers, realtors, appraisers, real estate companies, mortgage lenders, credit evaluators, government housing boards). So this form of evaluation aims to be objective and use mathematical inference of objectively estimate a value of a house based on historical transactions.

The effectiveness will be determined in the training set based on the difference between predicted house sale price and the actual sales price provided in the training data. Then evaluated from the test set by the same method. Root-Mean-Squared Error is used to determine the best training model.

#### 1.2.1 Assumptions:
- Historical records are still relevant in the future. Although the year sold is also taken into account
- All variables provided include all the relevant factors in determining the price of a house sold
- Ridge and Lasso regularisation is sufficient to reduce significant multicollinearity if present

### 1.3 Code files:
- `Project 2` - Main project note book
- `Train_Test_Split+MSE_Comparison.ipynb` - Applied Train-Test-Split and K-fold Cross Validation before comparing the aggregated scores with root mean squared error metric
- `Polynomial_test.ipynb` - evaluating power terms of `Gr Liv Area`, `Yr Built`

Please use `Project 2` as the first and main notebook and remainder as appendices.


### 1.4 Data Description:
- `train.csv` - the training set
- `test.csv` - the test set
- `data_description.txt` - full description of each column prepared by *Sidharth Kumar Mohanty* ([*source*](https://www.kaggle.com/sidharth178/top-10-house-price-prediction/data))
- `combined_df.csv` - all train and test data preprocessed
- `submission.csv` - a benchmark submission from a linear regression on $[insert-chosen-parameters]$

## 6. Model Development
6.0 established the OLS Baseline as a linear model with `Gr Liv Area` and `Year Built`. These are considered because in most property listings these are the two popular value metrics considering capacity and living condition. 

6.1 to 6.3 Linear Regression is applied across entire train data set. three linear regressions: OLS, RidgeCV, LassoCV are used. These three use linear regression as principle driver but vary in considering overfitting.

In deciding the submission model the below two files are used to obtain metrics to choose the best model ***RidgeCV***.

--- 

file: `Train_Test_Split+MSE_Comparison.ipynb`
- file is used to perform Train-test-split with K-fold validations to determine expecteded scores for a given model
- Then MSE comparison is used between models to find the model resulting in the lowest aggregate score ('neg_mean_squared_error')
Model with the *lowest and consistent mean CV score is chosen*. It is determined that ***RidgeCV*** is the most effective model

'*' Elasticnet is tested and it tended to full lasso regularisation. this is interesting because even though ElasticNet chooses the l1_ratio with the best score RidgeCV still has a better score than LassoCV. ElasticNet is dropped from further analysis.

--- 

file: `Polynomial_test.ipynb`
- analysis involved observing `Gr Liv Area` and `Year Built` is squared
- MSE for train and test did not significantly improve implying overfitting improvedments
The above two terms are rejected for the chosen model

---  

## 8. Conclusions
### 8.1.1 Recommendations
In terms of equality and housing valuations there is multi-level participation
1. authorities  
    a. continue audits  
    b. housing - ensure zoning is fair (quotas, subsidised rent/buy). Taking Ridge CV coefficients in table below some lessons can be provided for authorities on town planning for equality see section 8.1.2
2. buyers  
    a. to encourage fair pricing even in advantaged housing zones to be re-evaluated with objective credit and housing values. Including reducing mortgage deposit requirements for biased housing estates and reducing mortgage requirements in previoiusly disadvantaged households  
3. disadvantaged households  
    a. In event of reparations (or paying back) the loss incurred to the disadvantaged households using this model or can be verified by the above model with some margin of error.
4. Sellers  
    a. gain access to platforms with valuations immediately so they do not have to wait to sell their house to find their value  
    b. be able to collateralise or decollateralise their house whenever they need to

### 8.1.2 Coefficients
Taking Ridge CV coefficients
some lessons can be provided for authorities on town planning for equality:
1. The pricing of the following top 10 factors are should all be independent with race
2. Town planning of zones is very important, and if zones such as C and A have majority black populations they should have quotas in place until there is no need for gov intervention

### 8.3 Final Considerations
Analysis started considering that this data includes all factors that accounts for house sale price however the problem statement assumes that there is racial discrimination. While this dataset does not include the races of all the parties in the transaction this proves that one of the initial assumptions do not hold but predicted target price can aggregate this bias. Although some analysis can be done to adjust for discrimination for example including races of all parties involved in the transaction e.g. seller, buyer, agent