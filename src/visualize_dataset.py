from transform_rates import TransformRates 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.preprocessing import StandardScaler 
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from mlxtend.feature_selection import SequentialFeatureSelector as sfs
from sklearn.metrics import accuracy_score as acc
from sklearn.tree import DecisionTreeClassifier 
from sklearn.linear_model import PassiveAggressiveClassifier 
from sklearn.linear_model import RidgeClassifier 
from sklearn.neighbors import KNeighborsClassifier

class VisualizeDataset: 
    def __init__(self, videoDataset):
        self.video_game_dataset = videoDataset 
    
    # visualize the console variable to see if console variable distribution is within the distribution 
    def console_distribution(self):
        video_game_rating_train = self.video_game_dataset 

        PS4_NUM = len(video_game_rating_train[video_game_rating_train['console'] == 0])
        PS4_XBOX_NUM = len(video_game_rating_train[video_game_rating_train['console'] == 1])
        labels = ['Play Station 4', 'Play Station 4 and XBOX']
        values = [PS4_NUM, PS4_XBOX_NUM]

        plt.figure(figsize=(17, 5))
        plt.subplot(1,2,1)
        plt.pie(values, labels = labels, autopct='%1.2f%%')
        plt.title('Pie Chart: Console distribution of Video Games Rating Dataset')
        plt.show()

    # visualize rating distribution 
    def rating_distribution(self):
        video_game_rating_train = self.video_game_dataset 
        uniqueRatingVals = set(video_game_rating_train['esrb_rating'])
        countArr = []
        for rate_name in uniqueRatingVals:
            countArr.append(len(video_game_rating_train[video_game_rating_train['esrb_rating'] == rate_name]))
    
        plt.figure(figsize=(17, 5))
        plt.subplot(1, 2, 1)
        plt.bar(list(uniqueRatingVals), countArr, color = 'orange')
        plt.title(' Bar graph: Rating Distribution ')
        plt.grid(True)

        plt.subplot(1, 2, 2)
        plt.pie(countArr, labels = list(uniqueRatingVals), autopct='%1.2f%%')
        plt.title(' Pie chart: Rating Distribution ')
        plt.show()

    # plot cross_validation plot 
    def cross_validation(self):
        transformRates = TransformRates()
        video_game_rating_train = transformRates.transform_rates(self.video_game_dataset)
        # TODO: add the rating transform to the dataset
        # transform the esrb rating to numerical  
        plt.figure(figsize = (30, 30))
        featuresRequired = video_game_rating_train.columns[2:-1]
        sb.heatmap(video_game_rating_train[featuresRequired].corr(), annot = True)
        plt.show()

    # apply PCA on target to decide if the target is seperable 
    def target_pca(self):
        video_game_rating_train = self.video_game_dataset
        featuresRequired = video_game_rating_train.columns[2: -1]
        featureVector = np.array(video_game_rating_train[featuresRequired])

        stdSc = StandardScaler()
        featureVector = stdSc.fit_transform(featureVector)

        pca = PCA(n_components=2)
        pca.fit(featureVector)
        featureVector = pca.transform(featureVector)

        dimReducedDataFrame = pd.DataFrame(featureVector)
        dimReducedDataFrame['targets'] = video_game_rating_train['esrb_rating']
        dimReducedDataFrame = dimReducedDataFrame.rename(columns = {0: 'V1', 1: 'V2'})
        print(dimReducedDataFrame)

        plt.figure(figsize=(10, 10))
        sb.scatterplot(data=dimReducedDataFrame, x='V1', y='V2', hue='targets')
        plt.grid(True)
        plt.show()




