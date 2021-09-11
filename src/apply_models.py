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
from transform_rates import TransformRates
import joblib

class ApplyModel:
    def __init__(self):
        # create map of classifier name to classifier object 
        self.model_name_to_classifier = {
            'RANDOM_FOREST': RandomForestClassifier,
            'DECISION_TREES': DecisionTreeClassifier,
            'PASSIVE_AGGRESSIVE': PassiveAggressiveClassifier,
            'RIDGE': RidgeClassifier,
            'KNEIGHBORS': KNeighborsClassifier
        }
    
    # split train and test dataset 
    def get_train_and_test_dataset(self, video_game_data):
        video_game_rating_train = video_game_data 
        # transform the esrb_rating from character to number 
        transform_rating = TransformRates()
        video_game_rating_train = transform_rating.transform_rates(video_game_rating_train)
        video_game_model_dataset = video_game_rating_train.loc[:, 'console':'esrb_rating']
        video_game_model_dataset.info()
        X_train, X_test, y_train, y_test = train_test_split(
            video_game_model_dataset.values[:,:-1],
            video_game_model_dataset.values[:,-1:],
            test_size=0.25,
            random_state=42
        )

        y_train = y_train.ravel()
        y_test = y_test.ravel()

        return {
            'X_train': X_train,
            'X_test': X_test,
            'y_train': y_train,
            'y_test': y_test
        }

    # apply model to training set and get feature and accuracy 
    def apply_model(self, model_name: str, X_train, X_test, y_train, y_test): 
        classifier = self.model_name_to_classifier[model_name]()
        sfs_applied = sfs(
            classifier,
            k_features = 20,
            forward=True,
            floating=False,
            verbose=2,
            scoring='accuracy',
            cv=5
        )
        sfs_performed = sfs_applied.fit(X_train, y_train)
        feature_cols = list(sfs_performed.k_feature_idx_)

        new_classifier = self.model_name_to_classifier[model_name]()
        new_classifier.fit(X_train[:, feature_cols], y_train)
        y_train_pred = new_classifier.predict(X_train[:, feature_cols])
        filename = '' + model_name + '_model.joblib'
        joblib.dump(new_classifier, filename)
        y_test_pred = new_classifier.predict(X_test[:, feature_cols])
        training_accuracy = acc(y_train, y_train_pred)
        testing_accuracy = acc(y_test, y_test_pred)

        return {
            'feature_cols': feature_cols,
            'training_acc': training_accuracy,
            'testing_acc': testing_accuracy
        }





    