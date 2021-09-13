
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Web APIs & NLP


# Executive Summary

- In Natural Language Processing, the target is for computers to correctly interpret natural language e.g. an provide meaningful interpretation. In the case of this project the power of machine learning to classify phrases and sentences will be examined.
- Objective is to :  

    1. Determine effectiveness of python models at NLP and classification of socially defined online communities  
    2. To decide if there may be a redundancy in having subreddits   

- Data is extracted from the website [Reddit.com](https://www.reddit.com). Collecting the titles from the subreddits as documents.
- Two vectorisers `CountVectorizer` and `TfidfVectorizer` are considered for the model to analyse.
- Machine Learning Classifiers (`Naive Bayes`, `Random Forest`, `Adaboost`, `VotingClassifier`, `SVM` and `Logistic Regression`) will be considered to determine if a doc belongs to either subreddit.
- Data will be split into ***train*** and **test** sample. Models are trained on the ***train*** sample and used to predict the ***test*** sample. The best model is determined by **accuracy** in predicting the ***test*** sample.


## Problem Statement

- The Goal of this project is to use python code classifiers to determine if a subreddit title belongs to "stocks" or "StockMarket"
- Find the best model given the following tools
    vectorisers: `CountVectorizer`, `TfidfVectorizer`  
    Estimators: `Naive Bayes`, `Random Forest`, `Adaboost`, `VotingClassifier`, `SVM`, `Logistic Regression`
    
## Assumptions
1. All information needed for classification resides in the title which is transformed to lower-cased words. 
2. Lemmatising and Stemming was another stepped that was avoided during this project due to the short-lived nature of the posts, this so most of the posts will be current, the presence of past tense may be useful in classifying types of posts on each side. 

_Fixed Variables_
-  vectorisers - max_features = 500, stop_words = 'english'

# Conclusions 

The model with based on trials of: 

- Tokenizer/Vecotrizer: `CountVectorizer`, `TfidfVectorizer`  
- Estimators: `Naive Bayes`, `Random Forest`, `Adaboost`, `VotingClassifier`, `SVM`, `Logistic Regression`

The model with the best performance is: 
- CountVectorizer(stop_words = 'english',ngram_range=(1,5),max_features=3000)  
- Estimator: LogisticRegressionCV(cv=5,  random_state=42, max_iter=200,n_jobs=-1)

***Baseline accuracy is 0.5 and best model test score is 0.61 with 22.6% improvement.***

Objectives:
    1. Determine effectiveness of python models at NLP and classification of socially defined online communities  
    2. To decide if there may be a redundancy in having subreddits

***There is significant score improvement to the baseline of the model therefore the model can be useful to distinguish a subreddit however the error rate is still 39%. There appears to be a high amount of overlap in the topics and so the models find it hard to distinguish. However the content in the title may not be sufficient to prove that the groups are distinct. Other aspects such as media and length of selftext should be relevant but were not available due to the API restrictions.***

# Recommendations
1. EDA and project scores allude that high `max_feature` contributing to favourable scores because of the inclusion of more rare words (where `stocks` and `StockMarket` share many similar words).  Towards the end of the project, the `max_feature` hyperparameter appears to be very significant because as it was unlimited during the initial Logistic Regression fit there was an improvement in scores. Due to time constraints there was no further investigation on the relationship between `max_feature` and score. Further work may be done to try an expanded feature set against decision tree classifiers.

2. Although Stemming and Lemmatising was avoided for this analysis. It may be helpful to the model to allow for a more generalised regression. Also be able to consolidate words and reduce the need for so many features.

3. Further work can be done to compare the model Accuracy, Sensitivity and Specificity against human classifications in a blind test. Trails can be performed with the model and human trained or read the same number of articles and compare the scores. Additionally the current best model trained against a large sample can be used to see how the former scores differ.

---

### Datasets

Using Pushshift's API, you'll collect posts from `stocks`, `StockMarket` subreddits. Then it is compiled into one dataset [`data`](./data.csv). 

#### `data.csv` columns
`title` - contains str with a phrase or sentence
`stocks` - =1 if post is from `stocks` subreddit

---

## Tokenizer/Vectorizer and Hyperparameter trails

`code1` already included `GridSearch` of some models there are other models and hyperparameters are tested. `code1`,`code2`,`code3`,`code4`,`code5` iterations are based on token/vectorizer and hyperparameters are trailed. While you can review them in the folder all of their results will be reviewed in this notebook `code1`.

##### [code1.ipynb](code1.ipynb)
Finding testing 4 models. Tokenized and vectorized with with CountVectorizer  
- Tokenizer  
    CountVectorizer
- Model  
    4.1 Naive Bayes   
    4.2 Random Forest (GridSearch)  
    4.3 Adaboost(Decision Tree)  
    4.4 Voting Classifier (RandomForest, AdaBoost(Decision Tree))
    
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
    
*LogReg is an effective model*

---



---
DELETE BELOW BEFORE SUBMISSION
---

### Necessary Deliverables / Submission

- Code must be in at least one clearly commented Jupyter Notebook.
- A readme/executive summary in markdown.
- You must submit your slide deck as a PDF.
- Materials must be submitted by **9:30 AM on Friday, April 23rd**.

---

## Rubric
Your local instructor will evaluate your project (for the most part) using the following criteria.  You should make sure that you consider and/or follow most if not all of the considerations/recommendations outlined below **while** working through your project.

For Project 3 the evaluation categories are as follows:<br>
**The Data Science Process**
- Problem Statement
- Data Collection
- Data Cleaning & EDA
- Preprocessing & Modeling
- Evaluation and Conceptual Understanding
- Conclusion and Recommendations

**Organization and Professionalism**
- Organization
- Visualizations
- Python Syntax and Control Flow
- Presentation

**Scores will be out of 30 points based on the 10 categories in the rubric.** <br>
*3 points per section*<br>

| Score | Interpretation |
| --- | --- |
| **0** | *Project fails to meet the minimum requirements for this item.* |
| **1** | *Project meets the minimum requirements for this item, but falls significantly short of portfolio-ready expectations.* |
| **2** | *Project exceeds the minimum requirements for this item, but falls short of portfolio-ready expectations.* |
| **3** | *Project meets or exceeds portfolio-ready expectations; demonstrates a thorough understanding of every outlined consideration.* |


### The Data Science Process

**Problem Statement**
- Is it clear what the goal of the project is?
- What type of model will be developed?
- How will success be evaluated?
- Is the scope of the project appropriate?
- Is it clear who cares about this or why this is important to investigate?
- Does the student consider the audience and the primary and secondary stakeholders?

**Data Collection**
- Was enough data gathered to generate a significant result?
- Was data collected that was useful and relevant to the project?
- Was data collection and storage optimized through custom functions, pipelines, and/or automation?
- Was thought given to the server receiving the requests such as considering number of requests per second?

**Data Cleaning and EDA**
- Are missing values imputed/handled appropriately?
- Are distributions examined and described?
- Are outliers identified and addressed?
- Are appropriate summary statistics provided?
- Are steps taken during data cleaning and EDA framed appropriately?
- Does the student address whether or not they are likely to be able to answer their problem statement with the provided data given what they've discovered during EDA?

**Preprocessing and Modeling**
- Is text data successfully converted to a matrix representation?
- Are methods such as stop words, stemming, and lemmatization explored?
- Does the student properly split and/or sample the data for validation/training purposes?
- Does the student test and evaluate a variety of models to identify a production algorithm (**AT MINIMUM:** Bayes and one other model)?
- Does the student defend their choice of production model relevant to the data at hand and the problem?
- Does the student explain how the model works and evaluate its performance successes/downfalls?

**Evaluation and Conceptual Understanding**
- Does the student accurately identify and explain the baseline score?
- Does the student select and use metrics relevant to the problem objective?
- Does the student interpret the results of their model for purposes of inference?
- Is domain knowledge demonstrated when interpreting results?
- Does the student provide appropriate interpretation with regards to descriptive and inferential statistics?

**Conclusion and Recommendations**
- Does the student provide appropriate context to connect individual steps back to the overall project?
- Is it clear how the final recommendations were reached?
- Are the conclusions/recommendations clearly stated?
- Does the conclusion answer the original problem statement?
- Does the student address how findings of this research can be applied for the benefit of stakeholders?
- Are future steps to move the project forward identified?


### Organization and Professionalism

**Project Organization**
- Are modules imported correctly (using appropriate aliases)?
- Are data imported/saved using relative paths?
- Does the README provide a good executive summary of the project?
- Is markdown formatting used appropriately to structure notebooks?
- Are there an appropriate amount of comments to support the code?
- Are files & directories organized correctly?
- Are there unnecessary files included?
- Do files and directories have well-structured, appropriate, consistent names?

**Visualizations**
- Are sufficient visualizations provided?
- Do plots accurately demonstrate valid relationships?
- Are plots labeled properly?
- Are plots interpreted appropriately?
- Are plots formatted and scaled appropriately for inclusion in a notebook-based technical report?

**Python Syntax and Control Flow**
- Is care taken to write human readable code?
- Is the code syntactically correct (no runtime errors)?
- Does the code generate desired results (logically correct)?
- Does the code follows general best practices and style guidelines?
- Are Pandas functions used appropriately?
- Are `sklearn` and `NLTK` methods used appropriately?

**Presentation**
- Is the problem statement clearly presented?
- Does a strong narrative run through the presentation building toward a final conclusion?
- Are the conclusions/recommendations clearly stated?
- Is the level of technicality appropriate for the intended audience?
- Is the student substantially over or under time?
- Does the student appropriately pace their presentation?
- Does the student deliver their message with clarity and volume?
- Are appropriate visualizations generated for the intended audience?
- Are visualizations necessary and useful for supporting conclusions/explaining findings?


---

### Why did we choose this project for you?
This project covers three of the biggest concepts we cover in the class: Classification Modeling, Natural Language Processing and Data Wrangling/Acquisition.

Part 1 of the project focuses on **Data wrangling/gathering/acquisition**. This is a very important skill as not all the data you will need will be in clean CSVs or a single table in SQL.  There is a good chance that wherever you land you will have to gather some data from some unstructured/semi-structured sources; when possible, requesting information from an API, but often scraping it because they don't have an API (or it's terribly documented).

Part 2 of the project focuses on **Natural Language Processing** and converting standard text data (like Titles and Comments) into a format that allows us to analyze it and use it in modeling.

Part 3 of the project focuses on **Classification Modeling**.  Given that project 2 was a regression focused problem, we needed to give you a classification focused problem to practice the various models, means of assessment and preprocessing associated with classification.   
