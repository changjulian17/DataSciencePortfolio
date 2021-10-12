
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Web APIs & NLP


# Executive Summary

- In Natural Language Processing, the target is for computers to correctly interpret natural language e.g. an provide meaningful interpretation. In the case of this project the power of machine learning to classify phrases and sentences will be examined.
- Objective is to :  

    1. Determine effectiveness of python models at NLP and classification of socially defined online communities  
    2. To decide if there may be a redundancy in having subreddits   

- Data is extracted from the website [Reddit.com](https://www.reddit.com). Collecting the titles from the subreddits as documents.
- Two vectorisers `CountVectorizer` and `TfidfVectorizer` are considered for the model to analyse.
- Machine Learning Classifiers (`Naive Bayes`, `Random Forest`, `Adaboost`, `VotingClassifier`, `SVM` and `Logistic Regression`) will be considered to determine if a doc belongs to either subreddit.
- Data will be split into ***train*** and **test** sample. Models are trained on the ***train*** sample and used to predict the ***test*** sample. The best model is determined by **accuracy** in predicting the ***lowest difference in train and test scores*** this is due to the high overfitting seen in the models.

When reviewing the code, please just review `code1.ipynb` the remainder of the notebooks are considered to be appendices.

## Problem Statement

- The Goal of this project is to use python code classifiers to determine if a subreddit title belongs to "stocks" or "StockMarket"
- Find the best model given the following tools
    vectorisers: `CountVectorizer`, `TfidfVectorizer`  
    Estimators: `Naive Bayes`, `Random Forest`, `Adaboost`, `VotingClassifier`, `SVM`, `Logistic Regression`
    
## Assumptions
1. All information needed for classification resides in the title which is transformed to lower-cased words. 
2. Lemmatising and Stemming was another step that was avoided during this project due to the short-lived nature of the posts, this so most of the posts will be current, the presence of past tense may be useful in classifying types of posts on each side. 

_Fixed Variables_
-  vectorisers - max_features = 500, stop_words = 'english'


# Conclusions 

The model with based on trials of: 

- Tokenizer/Vecotrizer: `CountVectorizer`, `TfidfVectorizer`  
- Estimators: `Naive Bayes`, `Random Forest`, `Adaboost`, `VotingClassifier`, `SVM`, `Logistic Regression`

After trialling some range of datapoints, ngram, estimators, number of features, the model with the best performance is: 
- CountVectorizer(stop_words = 'english',ngram_range=(1,5),max_features=3000)  
- Estimator: RandomForestClassifier(random_state=42, max_depth=3, n_estimators=200,n_jobs=-1)

**Baseline accuracy is 0.5 and best model test score is 0.61 with 20% improvement.**

Objectives:
    1. Determine effectiveness of python models at NLP and classification of socially defined online communities  
    2. To decide if there may be a redundancy in having subreddits

**There is significant score improvement to the baseline of the model therefore the model can be useful to distinguish a subreddit however the error rate is still 39%. There appears to be a high amount of overlap in the topics and so the models find it hard to distinguish. However the content in the title may not be sufficient to prove that the groups are distinct. Other aspects such as media and length of selftext should be relevant but were not available due to the API restrictions.**

# Recommendations
1. EDA and project scores allude that high `max_feature` contributing to favourable scores because of the inclusion of more rare words (where `stocks` and `StockMarket` share many similar words).  Towards the end of the project, the `max_feature` hyperparameter appears to be very significant because as it was unlimited during the initial Logistic Regression fit there was an improvement in scores. However this lead to overfitting and the current model is still overfit. Including more information like self text or reading the images will help to provide more data to interpret the post.

2. Although Stemming and Lemmatising was avoided for this analysis. It may be helpful to the model to allow for a more generalised regression. Also be able to consolidate words and reduce the need for so many features.

3. Further work can be done to compare the model Accuracy, Sensitivity and Specificity against human classifications in a blind test. Trails can be performed with the model and human trained or read the same number of articles and compare the scores. Additionally the current best model trained against a large sample can be used to see how the former scores differ.
---

### Datasets

Using Pushshift's API, you'll collect posts from `stocks`, `StockMarket` subreddits. Then it is compiled into one dataset [`data`](./data.csv). 

#### `data.csv` columns
`title` - contains str with a phrase or sentence
`stocks` - =1 if post is from `stocks` subreddit

#### `best_model.joblib` model
Saved model

Results of multiple trails are saved in results folder:
[`code1_results.csv`]('./results/code1_results.csv')
[`code3_results.csv`]('./results/code1_results.csv')
[`code4_results.csv`]('./results/code1_results.csv')
[`code5_results.csv`]('./results/code1_results.csv')

---

## Tokenizer/Vectorizer and Hyperparameter trails

`code1` already included `GridSearch` of some models there are other models and hyperparameters are tested. `code1`,`code2`,`code3`,`code4`,`code5` iterations are based on token/vectorizer and hyperparameters are trailed. While you can review them in the folder all of their results will be reviewed in this notebook `code1`.

# Appendix A
##### [code1.ipynb](code1.ipynb)
Finding testing 4 models. Tokenized and vectorized with with CountVectorizer  
- Tokenizer  
    CountVectorizer
- Model  
    4.1 Random Forest (GridSearch)  
    4.2 Adaboost(Decision Tree)  
    
*Random Forest (RF) and Voting Classifier is the best but since voting classifier has the exact test score as RF then we can assume that AdaBoost has little effect (Except where VotingClassifier train score > RF train score) * 

#### [code2.ipynb](code2.ipynb)
Comparing results if `StockMarket` subreddit is swapped for `Paleontology`  
(both using CountVectorizer)

- Tokenizer  
    CountVectorizer
- Model  
    4.1 Naive Bayes   
    4.2 Random Forest (GridSearch)  
    4.3 Voting Classifier (RandomForest, AdaBoost(Decision Tree))
    
Taking Random Forest model comparing:
- `stocks`, `StockMarket` test score is 0.594
- `stocks`, `Paleontology` test score is 0.870  

Taking Voting Classifier model comparing:
- `stocks`, `StockMarket` test score is 0.594
- `stocks`, `Paleontology` test score is 0.870  


*The types of subreddits chosen will affect the accuracy of the classifier*

#### [code3.ipynb](code3.ipynb)
Trialed TF-IDF over CountVectorizer.  
- Tokenizer  
    TfidfVectorizer
- Model  
    4.1 Naive Bayes   
    4.2 Random Forest (GridSearch)  
    4.3 Adaboost(Decision Tree)  
    4.4 Voting Classifier (RandomForest, AdaBoost(Decision Tree))
    
*Best model found to be RF. Negligible change and slight decrease in test score.*

#### [code4.ipynb](code4.ipynb)

Trialed various n-grams with RF.  
Created an iterator for ngram  
    - (1, x), where x is 1 to 9  
    - (2, x), where x is 2 to 6  
    - (3, x), where x is 3 to 6   
Collate results

- Tokenizer  
    TfidfVectorizer
- Model  
    4.1 Random Forest (max_depth=20, n_estimators=100) 
    
*ngram (1,5) appears to be the best. increasing max ngram past does improve however this may be due to collinearity
increasing min ngram does not show to improve the performance*
    
#### [code5.ipynb](code5.ipynb)
Expanded code1 trials with two more models. Tokenized and vectorized with CountVectorizer
- Tokenizer  
    CountVectorizer (unlimited tokens ~2200 << # of rows ~1600)
- Model  
    4.1 Support Vector Machines    
    4.2 Logistic Regression 
    
LogReg is an effective model
    
*Random forest is chosen as the best model*
