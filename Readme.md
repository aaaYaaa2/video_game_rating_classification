# Video Games Rating By 'ESRB'

This repository is a basic analysis and prediction on Video Games Ratings By 'ESRB'. Base on the dataset provided in [kaggle](https://www.kaggle.com/imohtn/video-games-rating-by-esrb). The problem that the project is trying to solve is to provide a model that could best predict the rating based on various features provided by users. There is also a [simple code docs](./Code_docs.md).

## Video Games Dataset Description 

Video Games ESRB ratings dataset contains 1895 games with 34 of ESRB rating content with the name and console as feature for each game. Features of games included game console information, Alcohol, Blood content, violence and other rating sensitive content, which usually contribute to variance of final game rating. 

More detailed information on the dataset, 
``` text 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1895 entries, 0 to 1894
Data columns (total 34 columns):
title                       1895 non-null object
console                     1895 non-null int64
alcohol_reference           1895 non-null int64
animated_blood              1895 non-null int64
blood                       1895 non-null int64
blood_and_gore              1895 non-null int64
cartoon_violence            1895 non-null int64
crude_humor                 1895 non-null int64
drug_reference              1895 non-null int64
fantasy_violence            1895 non-null int64
intense_violence            1895 non-null int64
language                    1895 non-null int64
lyrics                      1895 non-null int64
mature_humor                1895 non-null int64
mild_blood                  1895 non-null int64
mild_cartoon_violence       1895 non-null int64
mild_fantasy_violence       1895 non-null int64
mild_language               1895 non-null int64
mild_lyrics                 1895 non-null int64
mild_suggestive_themes      1895 non-null int64
mild_violence               1895 non-null int64
no_descriptors              1895 non-null int64
nudity                      1895 non-null int64
partial_nudity              1895 non-null int64
sexual_content              1895 non-null int64
sexual_themes               1895 non-null int64
simulated_gambling          1895 non-null int64
strong_janguage             1895 non-null int64
strong_sexual_content       1895 non-null int64
suggestive_themes           1895 non-null int64
use_of_alcohol              1895 non-null int64
use_of_drugs_and_alcohol    1895 non-null int64
violence                    1895 non-null int64
esrb_rating                 1895 non-null object
dtypes: int64(32), object(2)
memory usage: 503.4+ KB
```

The above short description shed light of some characteristics for the dataset. There are 33 features of game, all of the features are represent in binary ( 0 or 1 ) with the meaning that certain feature present in the game or not. `esrb_rating` is the target variable that we would like to predict: with `E` represent 'Everyone', `ET` represent 'Everyone 10+', `T` represent 'Teen' and `M` represent 'Mature'. Except for target variable, other features are in `int64` and no null values in dataset. 

## Data Visualization 

In this section, more visualization of the dataset will be performed. 

*Visualize Console Feature*

Let's take a look at the `console` variable. `console` indicate which game console/platform game is published. 

![console_distribution](./images/console_distribution.png) 

The pie chart above shows that there are mainly two types console in the dataset, `Play Station 4` and `Play Station 4 and XBOX`. Games on `Play Station 4` only exceeds a little than games published on both player station 4 and Xbox. 


*Visualize Rating Distribution* 

Let's look at the target variable distribution, in both bar chart and pie chart. 

![bar_chart_pie_chart_rating](./images/bar_graph_rating.png)

`Mature`, `Everyone` and `Everyone 10+` are in similar number while `Teen` rating takes a slightly larger number than the rest categories. 

*Cross Validation Map*

The Cross Validation Map will show which features are highly correlated with target variables. 

![cross_validation](./images/cross_validation.png) 

There are several features that are of high correlation with target, `blood` with value of `0.43`, `blood_and_gore` with value of `0.45`, `strong language` with value of `0.5`, `no_descriptors` with value of `-0.54`. Other highly correlated features are `sexual_themes` with value of `0.27`, `intense_violence` with value of `0.25`, `strong_sexual_content` with value of `0.24` and `simulated_gambling` with value of `0.22`, `mild_fantasy_violence` with value of `-0.29`. On the other hand, there are some features that is of smaller correlation with target variable, for instance `animated_blood` with value of `-0.0025`, `mild_violance` with value of `-0.018`, `cartoon_violance` of value of `0.013`. 

*Visualize Target Variable*

The problem is to classify video games into various rating categories, but is the target separatable? In this section, we visualize target varaible to see if the target variable is suitable for classification, apply PCA algorithm to plot different categories on graph. 

![separatable_target](./images/pca_rating.png)

Observed from the above graph, we could see that the target could be separate into different clusters when project to different vectors. So classification algorithm would work in this case. 


## Classification Models 

There are several classification model that will be explored in this project. The dataset is split into testing and trainig. `Random Forest Classifier`, `Decision Tree Classifier`, `Passive Aggressive Classifier`, `Ridge Classifier` and `K Neighbors Classificier`. There are 33 features for prediction, we apply feature selection method to obtain a simpler model. 

*Random Forest* 

First we start with Random Forest prediction. The results is as follows: 
The features left are as follows ( features are represented in column indexes )

``` text 
    [1, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 26, 28]  
```

And `Training Accurarcy` and `Testing Accurarcy` are as follows 

```text
    Training accuracy on selected features: 0.793
    Testing accuracy on selected features: 0.766
```

*Decision Tree Classifier* 

The decision tree classifier is also a common classifier. Most important features are 

```text 
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 13, 16, 18, 19, 24, 25, 26, 27, 28, 29, 31] 
```

The training and testing accuracy are  

```text
    Training accuracy on selected features: 0.899
    Testing accuracy on selected features: 0.854
```

*Passive Aggressive Classifier*

The features selected by Passive Aggressive Classifier. 

```text
   [2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 18, 20, 21, 23, 24, 25, 26, 27, 28, 29] 
```

Training and testing accuracy are present in the following 
```
    Training accuracy on selected features: 0.785
    Testing accuracy on selected features: 0.785     
```

*Ridge Classifier*
```text
    [0, 1, 2, 3, 4, 5, 7, 8, 9, 12, 14, 15, 20, 21, 22, 24, 25, 26, 28, 29]
    Training accuracy on selected features: 0.785
    Testing accuracy on selected features: 0.776
```

*K Neighbors Classifier*

```text 
    [8, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31]
    Training accuracy on selected features: 0.716
    Testing accuracy on selected features: 0.681
```

From the previous model analysis, among the models, decision seems give the best performance accuracy, given by highest training and testing accuracy. 

There are several features that present in all models, for instance `9 - intense violence`, `13 - mild_blood`, `14 - mild_catoon_violence`, `15 - mild_fantary_violence`, `24 - sexual_theme`, `26 - strong_language` and `28 - suggestive_themes`. Those features overlaps with some of features discovered in cross-validation process. 
